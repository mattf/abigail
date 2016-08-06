#!/bin/python3

import argparse

DAYS = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')

def main(bitmap):
    with open(bitmap, 'r') as data:
        # bits[day of week][week of year]
        bits = list(map(list, data))
        print('touch wall; git add wall')
        for i, day in enumerate(DAYS):
            for j in range(52):
                if bits[i][j] is 'X':
                    for k in range(35 + 40):
                        print('echo %i,%i,%i > wall' % (i, j, k))
                        print('git commit --date="$(date --date="%s %i weeks ago")" -m . wall' % (day, 53 - j))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('bitmap', help='bitmap to spray')
    args = parser.parse_args()
    main(args.bitmap)
