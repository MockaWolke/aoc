from aoc import get_aoc_input

data = get_aoc_input(day=11, year=2023)
# Your solution starts here

lines = data.splitlines()
    
stars = list()
for y,line in enumerate(lines):
    for x,char in enumerate(line):
        if char == "#":
            stars.append((x,y))

y_expands = [y for y,line in enumerate(lines) if "#" not in line]
x_expands = [x  for x,_ in enumerate(lines[0]) if '#' not in "".join([line[x] for line in lines])]



def manhatten(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) 

def compute_part(FAC):
    new_cords = []

    for x,y in stars:
        x += max(len([i for i in x_expands if i < x]) * (FAC - 1), 0)
        y += max(len([i for i in y_expands if i < y]) * (FAC - 1), 0)
        new_cords.append((x,y))
    
    s = 0

    for a in new_cords:
        for b in new_cords:
            s += manhatten(a,b)
            
    print(s // 2)
    
    
compute_part(FAC = 2)
compute_part(FAC = 1000000)