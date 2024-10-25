
from math import sqrt, ceil
import re
from aoc.get_data import get_aoc_input

data = """Time:      7  15   30
Distance:  9  40  200"""
data = get_aoc_input(6, 2023)

lines = data.splitlines()

get_numbers = lambda x: list(map(int, re.findall(r"\d+", x)))
times, distances = map(get_numbers, lines)
races = list(zip(times, distances))


prod = 1

for time, distance in races:
    
    counter = 0
    
    for s in range(1, time):
        d = (time - s) * s
        if d > distance: counter += 1

    prod *= counter
print(prod)

lines = data.splitlines()

time, distance = get_numbers(data.replace(" ",""))

one = time/2 - sqrt((time/2 )**2 - distance )
two = time/2 + sqrt((time/2 )**2 - distance )


left = ceil(one)
right = ceil(two) 

print(time, distance)
print(right - left)