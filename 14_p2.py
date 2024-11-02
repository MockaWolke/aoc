from aoc import get_aoc_input
from pathlib import Path
from appdirs import user_cache_dir

data = get_aoc_input(day=14, year=2023)


data = data.splitlines()
DIM = len(data)
N_ITERATIONS = 1000000000

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

                

def pretty_print(prin = True):
    output = []
    for y in range(len(data)):
        s = ""
        for x, col in enumerate(cols):            
            if y in col:
                s += "O" 
            elif (x,y) in hard:
                s += "#" 
            else:
                s += "."
        if prin: print(s)
        output.append(s)
    if prin: print()
    return "\n".join(output)



def move():
    global cols
    for x, col in enumerate(cols):
        for i, val in enumerate(col):
            col[i] = find_closest(val, col, x)


def rotate_90(x,y):
  return DIM - 1- y, x  
    
def rotate():
    global hard, cols
    hard = {rotate_90(*i) for i in hard}
    
    n_cols = [[] for _ in range(DIM)]
    for x,c in enumerate(cols):
        for y in c:
            nx,ny = rotate_90(x,y)
            n_cols[nx].append(ny)
    for c in cols:
        c.sort()
    cols = n_cols


h1 = hash(pretty_print())
for _ in range(4):
    rotate()

h2 = hash(pretty_print())
assert h1 == h2, "Test failed"




cycles = {}
for i in range(N_ITERATIONS):
    for _ in range(4):
        move()
        rotate()
    
    h = hash(pretty_print(prin=False))
    if h in cycles and (N_ITERATIONS -1 - cycles[h] )% (i - cycles[h]) == 0 :
        break
    cycles[h] = i
    
    if i< 3:
        print(i)
        pretty_print()


def count():
    part2 = 0
    for x, col in enumerate(cols):
        for val in col:
            part2 += len(data) - val
    return part2
print(count())