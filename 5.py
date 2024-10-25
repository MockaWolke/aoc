import re
from aoc.get_data import get_aoc_input


data = get_aoc_input(5, 2023)

lines = data.splitlines()

get_numbers = lambda x: list(map(int, re.findall(r"\d+", x)))

seeds = get_numbers(lines[0])

mappings = {}
for l in data.split("\n\n")[1:]:
    l = l.splitlines()

    mapping = {}

    inputs = list(map(get_numbers, l[1:]))

    name = l[0].replace(" map:", "")
    mappings[name] = inputs

func = mappings["seed-to-soil"]


def get_location(seed):
    val = seed
    for _, mapping in mappings.items():
        for new, start, n in mapping:

            if val >= start and val < start + n:
                val = val - (start - new)
                break
    return val


res = min(get_location(s) for s in seeds)


def get_location2(pair):

    valid = [pair]
    for _, mapping in mappings.items():
        new_pairs = []

        while valid:

            l, end = valid.pop()
            r = end + l - 1
            for new, start, n in mapping:
                iend = start + n - 1

                # overlap
                left = max(l, start)
                right = min(r, iend)
                
                # if overlap
                if (
                    left >= start
                    and left < iend
                    and right >= start
                    and right <= iend
                    and right > left
                ):
                    length = right - left

                    new_pairs.append((left - (start - new), length))

                    if left > l:
                        valid.append((l, left - l))

                    if r > right:
                        valid.append((right + 1, r - right))

                    break
            else:
                new_pairs.append((l, end))

        valid = new_pairs
    return min(i[0] for i in valid)


pairs = zip(seeds[::2], seeds[1::2])

val = min(get_location2(i) for i in pairs)
print(val)
