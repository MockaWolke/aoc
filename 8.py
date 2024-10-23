from get_data import get_aoc_input
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

position = "AAA"
i = 0
while True:
    move = instructions[i]
    i = (i + 1 )% len(instructions)
    counter += 1
    print(position, move)
    position = nodes[position][0 if move == "L" else 1]
    print(position)
    if position == "ZZZ":
        break    
    
print(counter)