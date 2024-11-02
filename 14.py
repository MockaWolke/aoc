from aoc import get_aoc_input

# data = get_aoc_input(day=14, year=2023)
import time
# Your solution starts here
data = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""


data = data.splitlines()
DIM = len(data)

hard = {(x,y) for y,line in enumerate(data) for x,c in enumerate(line) if c == "#"}
# rows = [[i for i,c in enumerate(line) if c == "O"] for line in data]
cols = [[y for y,line in enumerate(data) if line[x] == "O" ]  for x in range(len(data[0]))]


def find_closest(val : int, col : list, x : int):
    if val == 0:
        return 0
    
    index = col.index(val)
    last_val = col[index - 1] if index != 0 else -1
    
    for y in range(val - 1, last_val, -1):
        if (x,y) in hard:
            return y + 1
    return last_val + 1

                

def pretty_print():
    for y in range(len(data)):
        s = ""
        for x, col in enumerate(cols):            
            if y in col:
                s += "O" 
            elif (x,y) in hard:
                s += "#" 
            else:
                s += "."
        print(s)


pretty_print()
print()

start = time.time()
part1 = 0
for x, col in enumerate(cols):
    for i, val in enumerate(col):
        col[i] = find_closest(val, col, x)
        part1 += len(data) - col[i] 


print(part1)
