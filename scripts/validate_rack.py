#!/usr/bin/env python3
"""Check that a hypothetical rack plan uses valid nonoverlapping U spaces."""
import csv,sys

def main(path):
    used={};errors=[]
    with open(path,newline='',encoding='utf-8') as fh:
        for row in csv.DictReader(fh):
            name=row['asset_id']
            try: start=int(row['first_u']);height=int(row['height_u'])
            except ValueError:
                errors.append(f'{name}: nonnumeric U');continue
            if height<=0 or start<1 or start+height-1>12:
                errors.append(f'{name}: outside 1–12U');continue
            for u in range(start,start+height):
                if u in used:errors.append(f'{name}: U{u} overlaps {used[u]}')
                else:used[u]=name
    if errors:
        print('INVALID RACK PLAN');print('\n'.join(errors));return 1
    print('VALID 12U plan; occupied:', ', '.join(f'U{u}={used[u]}' for u in sorted(used)))
    return 0
if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('Usage: python3 validate_rack.py rack_plan.csv')
    sys.exit(main(sys.argv[1]))
