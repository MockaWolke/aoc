from aoc import get_aoc_input
from helpers import get_2dmap, tuple_add


data = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""
data = get_aoc_input(21, 2023)

cords = get_2dmap(data.splitlines())
start = [i for i, v in cords.items() if v == "S"][0]
cords[start] = "."

transitions = {}
for tup, char in cords.items():
    if char != ".":
        continue

    valid = set()
    for diff in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        n = tuple_add(diff, tup)
        
        if n in cords and cords[n] == ".":
            valid.add(n)
    transitions[tup] = valid


current = {start}

for _ in range(64):
    
    new = set()
    for c in current:
        new.update(transitions[c])
    
    current = new
    
print(len(current))