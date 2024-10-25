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

goal_y = 10

lines = open("15.txt").read().splitlines()
goal_y = 2000000

coords = [list(map(int,re.findall(r'-?\d+',l))) for l in lines]

not_a_beacon = set()

def give_all_valid_manhatten(x,y,distance):

    res = []
    ny = goal_y

    if y-distance <= goal_y and goal_y <= y+distance:


        for nx in range(x-distance,x+distance+1):
           

                if abs(x-nx) + abs(y-ny) <= distance:
                    res.append((nx,ny))

    return res


for x,y, bx,by in tqdm.tqdm(coords):

    distance = abs(x-bx) + abs(y-by)
    res = give_all_valid_manhatten(x,y,distance)

    if (bx,by) in res:
        res.remove((bx,by))

    for val in res:
        not_a_beacon.add(val)



part1 = len(not_a_beacon)
print("Part 1:",part1)