from aoc import get_aoc_input


data = get_aoc_input(day=13, year=2023)
# Your solution starts here
# data = """#.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#"""

def check(rows):
    for yr in range(1, len(rows)):
        yl = yr - 1
        diff = 0
        
        while yl - diff >= 0 and yr + diff < len(rows):
            if rows[yl - diff] != rows[yr + diff]:
                break
            
            diff += 1
        else:
            return yr
        

val = 0        
for block in data.split("\n\n"):

    rows = [{i for i,c in enumerate(line) if c == "#"} for line in block.splitlines()]

    cols = [{y for y,line in enumerate(block.splitlines()) if line[x] == "#" }  for x in range(len(block.splitlines()[0]))]
    
    if v := check(cols):
        val += v
        continue
    
    if v := check(rows):
        val += v * 100
        continue
    
    print("nothing found!")
    
print(val)
    
def find_diff(rows):

    for yr in range(1, len(rows)):
        yl = yr - 1
        diff = 0
        
        val = None
        while yl - diff >= 0 and yr + diff < len(rows):

            difference = (rows[yl - diff] - rows[yr + diff]) | (rows[yr + diff] - rows[yl - diff])

            if len(difference) > 1 or (len(difference) == 1 and val is not None):
                break
            elif len(difference) == 1:
                val = (list(difference)[0], yl - diff, yr)
            
            diff += 1
            
        else:
            # print("hey?", val)
            if val is not None:
                return val
        
        
errors = []

val = 0        
for block in data.split("\n\n"):
    
    rows = [{i for i,c in enumerate(line) if c == "#"} for line in block.splitlines()]

    cols = [{y for y,line in enumerate(block.splitlines()) if line[x] == "#" }  for x in range(len(block.splitlines()[0]))]
    
    if (v := find_diff(cols)) is not None:
        val += v[-1]
        continue
    
    if (v := find_diff(rows)) is not None:
        val += v[-1] * 100
        continue
    
    errors.append(block)

with open("debug.txt", "w") as f:
    f.write("\n\n".join(errors))

print(val)