from aoc.get_data import get_aoc_input
import re

data = get_aoc_input(day = 4, year= 2023).splitlines()

points = 0


for line in data:
    
    line = line[line.find(":"):]
    winning, got = line.split("|")
    
    winning = set(map(int, re.findall(r"\d+", winning)))
    got = set(map(int, re.findall(r"\d+", got )))
    
    exponent = len(winning.intersection(got)) - 1
    points += 0 if exponent < 0 else 2 ** exponent

print(points)
