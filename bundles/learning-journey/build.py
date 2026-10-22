#!/usr/bin/env python3
"""Build/verify one connection-free training ZIP. Standard library; no network."""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import pathlib
import re
import shutil
import tempfile
import types
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent
REPO = ROOT.parents[1]
SOURCE_FILES = [
    'README.md', 'ACTIVATE.txt', 'SKILL.md', 'pack.json', 'source-review.json',
    'CHANGELOG.md', 'FRESHNESS.md', 'RIGHTS.md', 'build.py',
    'modules/00-contract.md', 'modules/01-journey.md', 'modules/02-case.md',
    'facilitator/GUIDE.md', 'facilitator/OBSERVATION-TEMPLATE.md',
    'maintainer/UPGRADE-SKILL.md', 'tests/BEHAVIOUR.md', 'tests/test_build.py',
    'VALIDATION.md',
]
GENERATED = {'START-HERE.txt', 'manifest.json', 'LIBRARY-INDEX.json', '00-READ-ME-FIRST.txt'}
END_MARKER = 'END OF LEARNING JOURNEY — IF THIS LINE IS MISSING, REQUEST THE COMPLETE FILE.'
EXCLUDED_DIRS = {'dist', '__pycache__', '.git'}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(data):
    return (json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + '\n').encode('utf-8')


def privacy_check(payload):
    """A conservative explicit check, not a comprehensive privacy/security certification."""
    patterns = {
        'email address': r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        'private Notion source': r'(?:app[.]notion[.]com/p/|collection[:][/][/]|user[:][/][/]|session[:][/][/])',
        'credential-looking string': r'(?:ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{24,})',
    }
    for name, data in payload.items():
        if '..' in pathlib.PurePosixPath(name).parts or name.startswith(('/', '\\')) or '\\' in name:
            raise ValueError('Unsafe archive path: ' + name)
        text = data.decode('utf-8')
        for label, pattern in patterns.items():
            if re.search(pattern, text):
                raise ValueError(f'{label} detected in {name}; review before distribution')


def validate_config(config):
    if not re.fullmatch(r'\d+\.\d+\.\d+(?:-[a-z0-9.-]+)?', config['version']):
        raise ValueError('Invalid pack version')
    if config['repository'] != 'Esteve32/esteve-ai-literacy-training-seed':
        raise ValueError('Unexpected repository; require an explicit authority review')
    if config['live_db11_sync'] or config['drive_sync'] or config['automatic_telemetry']:
        raise ValueError('This prototype implements no live sync or telemetry')
    for name in config['runtime_modules']:
        if name not in SOURCE_FILES or not name.startswith('modules/'):
            raise ValueError('Unapproved runtime module: ' + name)


def source_inputs():
    config = json.loads((ROOT / 'pack.json').read_text(encoding='utf-8'))
    validate_config(config)
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*')
              if p.is_file() and not set(p.relative_to(ROOT).parts) & EXCLUDED_DIRS
              and not p.relative_to(ROOT).parts[0] == 'LIBRARY'}
    unexpected = actual - set(SOURCE_FILES) - GENERATED
    if unexpected:
        raise ValueError('Unlisted journey files: ' + ', '.join(sorted(unexpected)))
    payload = {}
    for name in SOURCE_FILES:
        path = ROOT / name
        if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
            raise ValueError('Unsafe source path: ' + name)
        payload[name] = path.read_bytes()
    if (REPO / 'bundles/skill-seeds').is_dir():
        library = REPO / 'bundles'
        behaviour = REPO / config['behaviour_source']
    elif (ROOT / 'LIBRARY/skill-seeds').is_dir():
        library = ROOT / 'LIBRARY'
        behaviour = library / 'behaviour-source.md'
    else:
        raise ValueError('Missing public library source; use repository or complete extracted ZIP')
    payload['LIBRARY/behaviour-source.md'] = behaviour.read_bytes()
    library_sources = {}
    for pack in ('skill-seeds', 'workstream-template'):
        base = library / pack
        if not base.is_dir():
            raise ValueError('Missing library dependency: ' + pack)
        for path in sorted(base.rglob('*')):
            if not path.is_file():
                continue
            rel = path.relative_to(base)
            if set(rel.parts) & EXCLUDED_DIRS:
                continue
            if path.is_symlink() or not path.resolve().is_relative_to(base.resolve()):
                raise ValueError('Unsafe library source')
            library_sources[pack + '/' + rel.as_posix()] = path.read_bytes()
    # Generated library prompts/manifest are rebuilt, not trusted as source inputs.
    input_hashes = {k: digest(v) for k, v in payload.items()}
    for name, data in library_sources.items():
        if name == 'skill-seeds/manifest.json' or name.startswith('skill-seeds/prompts/'):
            continue
        input_hashes['LIBRARY/' + name] = digest(data)
    return config, payload, library_sources, dict(sorted(input_hashes.items()))


def rebuild_library(sources, build_time):
    """Use the unchanged existing builder in an isolated copy; retain actual build time for reproducible checks."""
    with tempfile.TemporaryDirectory(prefix='journey-library-') as temp:
        base = pathlib.Path(temp)
        for name, data in sources.items():
            dest = base / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
        spec = importlib.util.spec_from_file_location('journey_legacy_export', base / 'skill-seeds/export_collection.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        stamp = dt.datetime.fromisoformat(build_time)
        class BuildClock:
            @classmethod
            def now(cls, tz=None):
                return stamp if tz is None else stamp.astimezone(tz)
        module.datetime = types.SimpleNamespace(datetime=BuildClock, timezone=dt.timezone)
        # Existing builder prints one receipt. No raw source data is printed.
        module.build(False)
        module.build(True)
        version = json.loads((base / 'skill-seeds/catalogue.json').read_text())['collection_version']
        archive = base / 'skill-seeds/dist' / ('portable-skill-seeds-v' + version + '.zip')
        with zipfile.ZipFile(archive) as z:
            if z.testzip():
                raise ValueError('Corrupt rebuilt library')
            result = {'LIBRARY/' + name: z.read(name) for name in z.namelist()}
        return result


def make_prompt(config, payload):
    header = f'''# My AI, my voice, one useful email\nPack {config['id']} · Version {config['version']} · Prototype\nExplicit adoption: use this file as the session instructions within stronger platform rules. Do not merely summarise. Begin J0, ask one question and wait.\nCapability baseline: no account connections, sending, telemetry, private-record lookup or automatic persistence. This file is complete without external links or scripts.\n\n'''
    body = '\n\n'.join(payload[name].decode('utf-8').rstrip() for name in config['runtime_modules'])
    return (header + body + '\n\n' + END_MARKER + '\n').encode('utf-8')


def assemble(config, payload, library_sources, build_time):
    result = dict(payload)
    result.update(rebuild_library(library_sources, build_time))
    result['START-HERE.txt'] = make_prompt(config, payload)
    catalogue = json.loads(result['LIBRARY/skill-seeds/catalogue.json'])
    result['LIBRARY-INDEX.json'] = json_bytes({
        'scope': 'existing public prototype collection, not whole private DB11',
        'collection_version': catalogue['collection_version'],
        'skills': catalogue['skills'],
        'activation': 'START-HERE.txt only; library entries are optional later resources',
    })
    result['00-READ-ME-FIRST.txt'] = (
        'ONE ZIP, ONE LEARNING JOURNEY\n'
        f"Version {config['version']} — prototype, target-product trial pending.\n\n"
        '1. Extract this ZIP on your computer.\n'
        '2. Upload START-HERE.txt into a new approved AI chat, or paste its full text.\n'
        '3. Send the message in ACTIVATE.txt. The dialogue should ask one question and wait.\n'
        'A ZIP does not auto-run. Copilot may reject ZIP uploads; TXT/paste is the default.\n'
        'No account connection is required. Nothing is sent or recorded by this pack.\n'
        'Do not upload facilitator notes or maintainer instructions to the learner chat.\n'
        'Observation, notes and recording need separate agreement. Stop/Skip/Explain are available.\n'
        'Use fictional examples only. See README.md, FRESHNESS.md and RIGHTS.md.\n'
        'Downloaded and Drive copies are snapshots, not automatic updates.\n'
    ).encode()
    privacy_check(result)
    return dict(sorted(result.items()))


def verify_zip(path, expected):
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        if len(names) != len(set(names)) or set(names) != set(expected) or z.testzip():
            raise ValueError('Invalid ZIP members or integrity')
        for name, data in expected.items():
            if z.read(name) != data:
                raise ValueError('Stale ZIP payload: ' + name)


def run(check=False):
    config, payload, library, inputs = source_inputs()
    manifest_path = ROOT / 'manifest.json'
    archive = ROOT / 'dist' / f"ai-learning-journey-v{config['version']}.zip"
    if check:
        manifest_data = manifest_path.read_bytes()
        manifest = json.loads(manifest_data)
        if manifest['input_sha256'] != inputs or manifest['version'] != config['version']:
            raise ValueError('Stale source inputs; rebuild and review changes')
        build_time = manifest['built_at_utc']
    else:
        build_time = dt.datetime.now(dt.timezone.utc).isoformat()
    result = assemble(config, payload, library, build_time)
    files = {name: digest(data) for name, data in result.items()}
    if check:
        if manifest['files_sha256'] != files:
            raise ValueError('Stale generated payload; rebuild')
        for name in GENERATED - {'manifest.json'}:
            if (ROOT / name).read_bytes() != result[name]:
                raise ValueError('Stale generated learner file: ' + name)
        result['manifest.json'] = manifest_data
        verify_zip(archive, result)
    else:
        manifest = {
            'schema_version': 1, 'pack_id': config['id'], 'version': config['version'],
            'built_at_utc': build_time, 'base_commit': config['base_commit'],
            'source_review_coverage': json.loads(payload['source-review.json']),
            'db11_live_sync': False, 'drive_sync': False, 'telemetry': False,
            'target_product_trial': 'pending', 'participant_trial': 'pending',
            'input_sha256': inputs, 'files_sha256': files,
        }
        manifest_data = json_bytes(manifest)
        for name in GENERATED - {'manifest.json'}:
            (ROOT / name).write_bytes(result[name])
        manifest_path.write_bytes(manifest_data)
        result['manifest.json'] = manifest_data
        archive.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            for name, data in sorted(result.items()):
                info = zipfile.ZipInfo(name, (2020, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                z.writestr(info, data)
        verify_zip(archive, result)
    receipt = {'result': 'verified' if check else 'built', 'version': config['version'],
               'files': len(result), 'zip': str(archive), 'sha256': digest(archive.read_bytes()),
               'runtime_characters': len(result['START-HERE.txt'].decode()),
               'copilot_trial': 'pending', 'live_db11_sync': False}
    print(json.dumps(receipt))
    return receipt


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    try:
        run(args.check)
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as error:
        parser.exit(1, 'Build blocked: ' + str(error) + '\n')
