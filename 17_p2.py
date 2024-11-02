from aoc import get_aoc_input
from heapq import heapify, heappop, heappush
from helpers import highlight, get_2dmap


data = """2413432311323
3214453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""


data = get_aoc_input(day=17, year=2023)
# Your solution starts here

data = data.splitlines()

MAX__X = len(data[0])

cords = get_2dmap(data, transform=int)


def get_dicrection(pos):
    x, y, ox, oy = pos

    if ox < x:
        return "right"
    if oy < y:
        return "down"
    if ox > x:
        return "left"
    if oy > y:
        return "down"
    raise ValueError("WTF!")


def get_transitions(pos):
    x, y, ox, oy, n, _ = pos

    res = []
    direction = get_dicrection(pos[:4])
    
    if (x,y) == (0,0):
        res.append((x + 4, y, x, y, 4))
        res.append((x, y + 4, x, y, 4))
        return res
    
    if n < 10:
        x_diff = (x - ox) // abs((x - ox)) if x != ox else 0
        y_diff = (y - oy) // abs((y - oy)) if y != oy else 0
        res.append((x + x_diff, y + y_diff, x, y, n + 1))

    if direction in ["up", "down"]:
        res.append((x + 4, y, x, y, 4))
        res.append((x - 4, y, x, y, 4))

    if direction in ["right", "left"]:
        res.append((x, y + 4, x, y, 4))
        res.append((x, y - 4, x, y, 4))

    return res


def search():
    queue = [(0, (0, 0, 0, -1, 0, tuple())),]
    heapify(queue)

    been_there = {}

    while queue:

        cost, pos = heappop(queue)
        direction = get_dicrection(pos[:4])
        previous_cost = been_there.get(pos[:2] + (direction,))


        if previous_cost is not None and previous_cost[0] <= cost and previous_cost[1] <= pos[4] and cost > 0:
            continue

        if pos[:2] == (MAX__X - 1, len(data) - 1):
            return cost, pos[-1]

        been_there[pos[:2] + (direction,)] = (cost, pos[4])

        for new in get_transitions(pos):

            if cords.get(new[:2]) is None:
                continue
            
            between = tuple()
            
            n_cost = 0
            
            if abs(new[0] - pos[0]) > 1:
                
                diff = 1 if new[0] > pos[0] else -1
                # print(pos[0], new[0], list(range(pos[0] + diff, new[0] + diff, diff)))
                for x in range(pos[0] + diff, new[0] + diff, diff):
                    between = between + (x,new[1])
                    n_cost += cords[(x,new[1])]

            elif abs(new[1] - pos[1]) > 1:
                diff = 1 if new[1] > pos[1] else -1
                # print(pos[1], new[1], list(range(pos[1] + diff, new[1] + diff, diff)))
                
                for y in range(pos[1] + diff, new[1] + diff, diff):
                    between += (new[0],y)
                    n_cost += cords[(new[0],y)] 
            
            else:
                n_cost += cords.get(new[:2])
            
            # print(n_cost, direction)
            # for y, line in enumerate(data):
                # s = ""
                # for x, c in enumerate(line):
                    # if (x,y) == pos[:2]:
                        # s += highlight(c, "RED")
                        # continue
                    # s += highlight(c, "GREEN") if (x, y) == new[:2] else c
                # print(s)
                    

            if abs(new[0] - pos[0]) > 1 and abs(new[1] - pos[1]) > 1:
                print("WTF!")


            heappush(queue, (n_cost + cost, new + (pos[-1] + between + new[:2],)))


cost, history = search()
history = {(x, y) for x, y in zip(history[::2], history[1::2])}

v = 0
for y, line in enumerate(data):
    s = ""
    for x, c in enumerate(line):
        s += highlight(c, "GREEN") if (x, y) in history else c
        v += cords[(x,y)] if (x, y) in history else 0 
        
        
    print(s)

print(cost)
print(v)