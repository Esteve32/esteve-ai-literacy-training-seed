#!/usr/bin/env python3
"""Demonstrate a verified positive-before / negative-after calendar-date convention."""
import argparse,datetime,json,sys
def derive(anchor,offset_days):
    if not isinstance(offset_days,int) or isinstance(offset_days,bool):raise ValueError('Offset must be an integer')
    date=datetime.date.fromisoformat(anchor)
    return (date-datetime.timedelta(days=offset_days)).isoformat()
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('anchor');p.add_argument('offset_days',type=int);a=p.parse_args()
    try:print(json.dumps({'anchor':a.anchor,'offset_days':a.offset_days,'derived':derive(a.anchor,a.offset_days),'scope':'read-only calendar-date example; confirm local convention; no business-day calendar or writes'}))
    except (ValueError,OverflowError) as e:print('Date demonstration blocked: '+str(e),file=sys.stderr);sys.exit(1)
