#!/usr/bin/env python3
"""Count visible Unicode code points in strict GBR XML-like interchange text."""
import argparse, json, math, sys, xml.etree.ElementTree as ET
COLOURS={'g':'green','b':'blue','r':'red'}
WRAPPERS={'L'+str(i) for i in range(1,9)}
def measure(text,ideal=(75,20,5)):
    if len(ideal)!=3 or any(not math.isfinite(x) or x<0 for x in ideal) or not math.isclose(sum(ideal),100,abs_tol=1e-9):
        raise ValueError('Reference mix must contain three finite non-negative values summing to 100')
    if '<!' in text or '<?' in text:raise ValueError('Declarations, comments and entities are not accepted')
    try:root=ET.fromstring('<root>'+text+'</root>')
    except ET.ParseError as exc:raise ValueError('Malformed tagged text') from exc
    counts={v:0 for v in COLOURS.values()}
    def add(value,active):
        if not value:return
        if active:counts[active]+=len(value)
        elif value.strip():raise ValueError('Non-whitespace text outside colour tags')
    def visit(node,active=None):
        if node.attrib:raise ValueError('Attributes are not accepted')
        if node.tag in COLOURS:
            if active:raise ValueError('Nested colour tags would double-count')
            active=COLOURS[node.tag]
        elif node.tag not in WRAPPERS and node.tag!='root':raise ValueError('Unknown tag: '+node.tag)
        add(node.text,active)
        for child in node:
            visit(child,active);add(child.tail,active)
    visit(root);total=sum(counts.values())
    if not total:raise ValueError('Empty coloured denominator')
    percentages={c:n*100/total for c,n in counts.items()}
    reference=dict(zip(('green','blue','red'),ideal))
    return {'counts':counts,'total':total,'percentages':percentages,'reference_percentages':reference,'delta_percentage_points':{c:percentages[c]-reference[c] for c in counts},'convention':'Unicode code points inside colour tags; XML entities decoded; external whitespace excluded','warning':'Descriptive text counts, not a validated quality or people score'}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--text');p.add_argument('--ideal',nargs=3,type=float,default=(75,20,5));a=p.parse_args()
    try:print(json.dumps(measure(a.text if a.text is not None else sys.stdin.read(),a.ideal),ensure_ascii=False,indent=2))
    except ValueError as exc:print('Count blocked: '+str(exc),file=sys.stderr);sys.exit(1)
