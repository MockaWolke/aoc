from aoc import get_aoc_input
from heapq import heapify, heappop, heappush
from helpers import highlight


data = """2413432311323
3215453535623
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
data = get_aoc_input(day=17, year=  2023)
# Your solution starts here

data = data.splitlines()

MAX__X = len(data[0])

cords = {(x, y): int(c) for y, line in enumerate(data) for x, c in enumerate(line)}


def get_dicrection(pos):
    x, y, ox, oy = pos

    if ox < x:
        return "right"
    if oy < y:
        return "down"
    if ox > x:
        return "left"
    return "up"


def get_transitions(pos):
    x, y, ox, oy, n, _ = pos

    res = []

    direction = get_dicrection(pos[:4])

    if n < 2:
        res.append((x + (x - ox), y + (y - oy), x, y, n + 1))

    if direction in ["up", "down"]:
        res.append((x + 1, y, x, y, 0))
        res.append((x - 1, y, x, y, 0))

    if direction in ["right", "left"]:
        res.append((x, y + 1, x, y, 0))
        res.append((x, y - 1, x, y, 0))

    return res


def search():
    queue = [(0, (0, 0, 0, -1, 0, tuple())), (0, (0, 0, -1, 0, 0, tuple())),]
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

            n_cost = cords.get(new[:2])

            if n_cost is None:
                continue

            heappush(queue, (n_cost + cost, new + (pos[-1] + new[:2],)))


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