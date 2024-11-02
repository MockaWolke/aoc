from aoc import get_aoc_input
from collections import deque
data = get_aoc_input(day=16, year=2023)


data = data.splitlines()
MAX_X = len(data[0])

cords = {(x, y): c for y, line in enumerate(data) for x, c in enumerate(line)}


def get_dicrection(pos):
    x, y, ox, oy = pos

    if ox < x:
        return "right"
    if oy < y:
        return "down"
    if ox > x:
        return "left"
    return "up"


def get_new_positions(pos):
    x, y, ox, oy = pos
    direction = get_dicrection(pos)
    char = cords[(x, y)]

    if (
        char == "."
        or (direction in ["left", "right"] and char == "-")
        or (direction in ["up", "down"] and char == "|")
    ):
        return [(x + (x - ox), y + (y - oy), x, y)]

    if char == "-":
        return [
            (x - 1, y, x, y),
            (x + 1, y, x, y),
        ]

    if char == "|":
        return [
            (x, y - 1, x, y),
            (x, y + 1, x, y),
        ]

    displace_ment = {
        "left": (0, 1),
        "right": (0, -1),
        "down": (-1, 0),
        "up": (1, 0),
    }[direction]
    if char == "/":
        return [(x + displace_ment[0], y + displace_ment[1], x, y)]

    if char != "\\":
        print("wtf")
    return [(x + displace_ment[0] * -1, y + displace_ment[1] * -1, x, y)]


def get_val(start_pos):
    lasers_positions = deque([start_pos])
    lid = set()
    before = set()

    while lasers_positions:
        cur = lasers_positions.popleft()
        direction = get_dicrection(cur)

        if (m := cur[:2] + (direction,)) in before:
            continue

        before.add(m)

        lid.add(cur[:2])

        for new in get_new_positions(cur):
            x, y = new[:2]
            direction = get_dicrection(new)
            if (
                x < 0
                or x >= MAX_X
                or y < 0
                or y >= len(data)
                or (x, y, direction) in before
            ):
                continue
            lasers_positions.append(new)

    return len(lid)


part1 = get_val((0, 0, -1, 0))
print(part1)


settings = (
    [(0, y, -1, y) for y in range(len(data))]
    + [(MAX_X - 1, y, MAX_X, y) for y in range(len(data))]
    + [(x, 0, x, -1) for x in range(MAX_X)]
    + [(x, len(data) - 1, x, len(data)) for x in range(MAX_X)]
)

part2 = max(get_val(setting) for setting in settings)

print(part2)
