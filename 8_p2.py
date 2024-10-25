from aoc.get_data import get_aoc_input
from math import lcm
data = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

data = get_aoc_input(8, 2023)
instructions = data.splitlines()[0].strip()

nodes = {}

for l in data.splitlines()[2:]:
    
    title, rest = l.split(" = ")
    l,r = rest[1:-1].split(", ")
    
    nodes[title] = (l, r)
    
counter = 0


def first_z(position):
    counter = 0

    while True:
        move = instructions[counter % len(instructions)]
        counter += 1
        position = nodes[position][0 if move == "L" else 1]
        if position.endswith("Z"):
            return counter, position            

def find_loop(counter, position):
    start = position
    while True:
        move = instructions[counter % len(instructions)]
        counter += 1
        position = nodes[position][0 if move == "L" else 1]
        if position == start:
            return counter, position            
    

def get_loop_length(start_position):
    
    counter, position = first_z(start_position)
    second_counter, position = find_loop(counter, position)
    assert second_counter / counter == 2
    return counter
    
positions = [node for node in nodes if node[-1]=="A"]

loop_lengths = [get_loop_length(p) for p in positions]
print(lcm(*loop_lengths))