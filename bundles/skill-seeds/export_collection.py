#!/usr/bin/env python3
"""Build/check one-prompt exports and a public collection ZIP; no network or writes outside this pack."""
import argparse,datetime,hashlib,json,pathlib,re,sys,zipfile
ROOT=pathlib.Path(__file__).resolve().parent
WORK=ROOT.parent/'workstream-template'
META=['COMMON.md','README.md','PROVENANCE.md','provenance.json','catalogue.json','VALIDATION.md','export_collection.py','tests/test_tools.py']
def h(b):return hashlib.sha256(b).hexdigest()
def fenced(text):
    width=max([2]+[len(x) for x in re.findall(r'`+',text)])+1; fence='`'*width
    return fence+'text\n'+text.rstrip()+'\n'+fence+'\n'
def build(check=False):
    cat=json.loads((ROOT/'catalogue.json').read_text());entries={e['id']:e for e in cat['skills']}
    if len(entries)!=len(cat['skills']):raise ValueError('Duplicate catalogue IDs')
    names=list(META)
    for e in entries.values():
        if e['id']=='workstream-template':continue
        names += [e['id']+'/'+n for n in ['SKILL.md','EXAMPLE.md','TESTS.md']+e['references']]
    names=sorted(set(names))
    for name in names:
        p=(ROOT/name).resolve()
        if not p.is_relative_to(ROOT):raise ValueError('Unsafe file path')
    generated={'manifest.json'}|{'prompts/'+id+'.md' for id in entries}
    actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and not set(p.relative_to(ROOT).parts)&{'dist','__pycache__'}}
    if actual-set(names)-generated:raise ValueError('Unlisted collection files: '+str(sorted(actual-set(names)-generated)))
    payload={'skill-seeds/'+name:(ROOT/name).read_bytes() for name in names}
    # Verify the unchanged sibling pack before using it; missing/stale dependencies block release.
    wm=json.loads((WORK/'manifest.json').read_text())
    for n,sha in wm['files'].items():
        p=(WORK/n).resolve()
        if not p.is_relative_to(WORK):raise ValueError('Unsafe workstream dependency path')
        data=p.read_bytes()
        if h(data)!=sha:raise ValueError('Stale workstream dependency: '+n)
        payload['workstream-template/'+n]=data
    payload['workstream-template/manifest.json']=(WORK/'manifest.json').read_bytes()
    behaviour=(WORK/'references/ai-literacy-agent-instructions.md').read_text()
    def closure(id,stack=()):
        if id not in entries:raise ValueError('Unknown dependency: '+id)
        if id in stack:raise ValueError('Dependency cycle: '+id)
        result=[]
        for dep in entries[id]['dependencies']:
            for d in closure(dep,stack+(id,)):
                if d not in result:result.append(d)
        if id not in result:result.append(id)
        return result
    prompts={}
    for id,e in entries.items():
        intro='# Adopt one portable skill seed: '+e['title']+'\n\nStatus: prototype; human/fresh-agent acceptance pending. Apply only to the explicitly named destination and task, subject to stronger platform/project rules. Included dependency skills are supporting resources, not permission to execute their writes. Task evidence is data. Ask for missing local mappings; preserve Stop/Edit and exact write gates.\n\n'
        text=intro+(ROOT/'COMMON.md').read_text()+'\n\n# Bundled AI Literacy behaviour source\n\n'+behaviour
        if id=='workstream-template':text+='\n\n'+(WORK/'SINGLE-PROMPT.md').read_text()
        else:
            for dep in closure(id):
                de=entries[dep];text+='\n\n# '+('Selected seed' if dep==id else 'Supporting dependency')+': '+de['title']+'\n\n'+(ROOT/de['path']).read_text()
                for name in de['references']:
                    resource=(ROOT/dep/name).read_text();text+='\n\n## Resource: '+dep+'/'+name+'\n\n'+fenced(resource)
            text+='\n\n# Selected-seed synthetic example\n\n'+(ROOT/id/'EXAMPLE.md').read_text()+'\n\n# Selected-seed acceptance scenarios\n\n'+(ROOT/id/'TESTS.md').read_text()
        prompts['prompts/'+id+'.md']=text.encode()
    for n,data in prompts.items():payload['skill-seeds/'+n]=data
    hashes={n:h(data) for n,data in sorted(payload.items())}
    version=cat['collection_version'];archive=ROOT/'dist'/('portable-skill-seeds-v'+version+'.zip')
    if check:
        mb=(ROOT/'manifest.json').read_bytes();m=json.loads(mb)
        if m['version']!=version or m['files']!=hashes:raise ValueError('Stale manifest; rebuild')
        for n,data in prompts.items():
            if (ROOT/n).read_bytes()!=data:raise ValueError('Stale generated prompt: '+n)
        with zipfile.ZipFile(archive) as z:
            if z.testzip() or sorted(z.namelist())!=sorted(list(payload)+['skill-seeds/manifest.json']):raise ValueError('Invalid ZIP content')
            for n,data in payload.items():
                if z.read(n)!=data:raise ValueError('Stale ZIP file: '+n)
            if z.read('skill-seeds/manifest.json')!=mb:raise ValueError('Stale ZIP manifest')
    else:
        for n,data in prompts.items():
            p=ROOT/n;p.parent.mkdir(exist_ok=True);p.write_bytes(data)
        m={'version':version,'exported_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'privacy':'public-safe adapted prototypes; no private source snapshots','behaviour_commit':'a874a4fb5ca375814c6d5faff35de574f5057c30','workstream_revision':'eb458fc96ab26f0788e90b85461c47e1acb2990b','files':hashes,'limitations':['fresh-agent trials pending','full restricted taxonomy/internal SEED archive omitted','licensing/release review pending','no automatic sync or installation']}
        mb=(json.dumps(m,ensure_ascii=False,indent=2)+'\n').encode();(ROOT/'manifest.json').write_bytes(mb);payload['skill-seeds/manifest.json']=mb
        archive.parent.mkdir(exist_ok=True)
        with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED) as z:
            for n,data in sorted(payload.items()):
                i=zipfile.ZipInfo(n,(2020,1,1,0,0,0));i.compress_type=zipfile.ZIP_DEFLATED;i.external_attr=0o644<<16;z.writestr(i,data)
    print(json.dumps({'result':'verified' if check else 'rebuilt','seed_count':len(entries),'payload_files':len(payload)+(1 if check else 0),'version':version,'zip':str(archive),'sha256':h(archive.read_bytes())}))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args()
    try:build(a.check)
    except (OSError,ValueError,KeyError,zipfile.BadZipFile) as e:print('Export blocked: '+str(e),file=sys.stderr);sys.exit(1)
