import re

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

10R5L5R10L4R5L5""".split("\n\n")

lines = open('22.txt').read().split("\n\n")

field,instructions = lines
field = field.splitlines()

instructions = re.sub(r"[A-Z]",lambda matchobj: f" {matchobj.group(0)} ",instructions).split()

field_map = {(x,y):c for y,line in enumerate(field) for x,c in enumerate(line) if c!=" "}
rows = {y:{x for x,c in enumerate(line) if c!=" "} for y,line in enumerate(field) }
columns = {x:{y for y in range(len(field)) if len(field[y]) > x and field[y][x]!=" "} for x in range(len(field[0]))}

def move(x,y,direction):

    nx,ny = 0,0

    if direction ==0:
        nx,ny = x+1,y

        if (nx,ny) not in field_map:
            nx = min(rows[y])

    elif direction ==1:
        nx,ny = x,y+1

        if (nx,ny) not in field_map:
            ny = min(columns[x])

    elif direction ==2:
        nx,ny = x-1,y

        if (nx,ny) not in field_map:
            nx = max(rows[y])

    elif direction ==3:
        nx,ny = x,y-1

        if (nx,ny) not in field_map:
            ny = max(columns[x])

    if field_map[(nx,ny)]=='#':
        return False
    
    return (nx,ny)


x,y = min(rows[0]),0

direction = 0

for instr in instructions:

    if instr=="R":
        direction = (direction+1)%4
        continue
    elif instr=="L":
        direction = (direction-1)%4
        continue

    instr = int(instr)

    for _ in range(instr):
        
        val = move(x,y,direction)

        if not val:
            break

        x,y = val

score = (y+1)*1000 + (x+1) * 4 + direction
print(x,y)
print("Part 1: ",score)
    
    

    