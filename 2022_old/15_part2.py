# import numpy as np
import re
import tqdm

lines = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".splitlines()

boundary = 20
lines = open("15.txt").read().splitlines()
boundary = 4000000


coords = [list(map(int,re.findall(r'-?\d+',l))) for l in lines]
not_a_beacon = [[] for y in range (boundary+1)]


def get_border_cases(x,y,distance):

    for ny in (range(max(y-distance,0), min(y+distance+1,boundary+1))):

        y_displacement = abs(y-ny)

        right_x = min(x+distance+1-y_displacement,boundary)
        left_x = max(x-distance + y_displacement,0)

        not_a_beacon[ny].append((left_x,right_x))


for x,y, bx,by in tqdm.tqdm(coords,desc='Sift through sensors'):

    distance = abs(x-bx) + abs(y-by)
    get_border_cases(x,y,distance)


def merge(l:list):
    l = l.copy()
    distinct = l.pop(0)
    while l:
        for i in range(len(l)):
            min_x,max_x = l[i]
            if distinct[0] <= min_x <= distinct[1] or distinct[0] <= max_x <= distinct[1] or min_x <= distinct[1] <= max_x or min_x <= distinct[0] <= max_x:
                distinct = (min(min_x,distinct[0]),max(max_x,distinct[1]))
                l.pop(i)
                break
        else:
            print(distinct,l)
            return distinct
    return False


for i,l in enumerate(tqdm.tqdm(not_a_beacon,desc="Search for beacon")):
    val = merge(l)
    if val:
        x = val[1]  if val[0]==0 else val[0]-1

        print("Part 2:",x*4000000+(i))
        print(val)
        break
