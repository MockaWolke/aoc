import re
import numpy as np
import os
from cubes import *

lines = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5""".split(
    "\n\n"
)
cube = test_cube

lines = open('22.txt').read().split("\n\n")
cube = real_cube

field, instructions = lines
field = field.splitlines()

instructions = re.sub(
    r"[A-Z]", lambda matchobj: f" {matchobj.group(0)} ", instructions
).split()

field_map = {
    (x, y): c for y, line in enumerate(field) for x, c in enumerate(line) if c != " "
}

max_x = max(i[0] for i in field_map.keys()) + 1
max_y = len(field)

cube_dim = int(np.sqrt(len(field_map) / 6))
print(cube_dim)
# cube_topology = np.array([[(x,y) in field_map for x in range(0,max_x,cube_dim)]for y in range(0,max_y,cube_dim)])
# print(cube_topology)
# cube_topology = {(x,y):True for y,line in enumerate(cube_topology) for x,c in enumerate(line) if c}
# print(cube_topology)
# exit()

rows = {y: {x for x, c in enumerate(line) if c != " "} for y, line in enumerate(field)}
columns = {
    x: {y for y in range(len(field)) if len(field[y]) > x and field[y][x] != " "}
    for x in range(len(field[0]))
}


def move(x, y, direction):
    # print(x,y)
    nx, ny = 0, 0

    if direction == 0:
        nx, ny = x + 1, y

    elif direction == 1:
        nx, ny = x, y + 1

    elif direction == 2:
        nx, ny = x - 1, y

    elif direction == 3:
        nx, ny = x, y - 1

    if (nx, ny) not in field_map:

        dir_name = direction_to_name[direction]

        block_coords = x // cube_dim, y // cube_dim
        
        try:
            new_block, new_direction, flip = cube[block_coords][dir_name]
        except:
            print(block_coords,dir_name)
            exit()
            
        # capture x
        if dir_name in ["u", "d"]:
            val = nx % cube_dim
        else:  # capture y
            val = ny % cube_dim

        # flip if needed for node
        if flip:
            val = cube_dim - 1 - val

        if new_direction == "d":
            ny = new_block[1] * cube_dim
            nx = new_block[0] * cube_dim + val
        elif new_direction == "u":
            ny = new_block[1] * cube_dim + cube_dim - 1
            nx = new_block[0] * cube_dim + val
        elif new_direction == "l":
            ny = new_block[1] * cube_dim + val
            nx = new_block[0] * cube_dim + cube_dim - 1
        elif new_direction == "r":
            ny = new_block[1] * cube_dim + val
            nx = new_block[0] * cube_dim
            
        direction = name_to_direction[new_direction]

    if field_map[(nx, ny)] == "#":
        return False

    return (nx, ny), direction


x, y = min(rows[0]), 0

direction = 0

for instr in instructions:

    if instr == "R":
        direction = (direction + 1) % 4
        continue
    elif instr == "L":
        direction = (direction - 1) % 4
        continue

    instr = int(instr)

    for _ in range(instr):

        val = move(x, y, direction)

        if not val:
            break

        (x, y),direction = val

score = (y + 1) * 1000 + (x + 1) * 4 + direction
print(x, y)
print("Part 2: ", score)
