from get_data import get_aoc_input
import re

data = get_aoc_input(day = 4, year= 2023).splitlines()

def get_score(line):
    
    line = line[line.find(":"):]
    winning, got = line.split("|")
    
    winning = set(map(int, re.findall(r"\d+", winning)))
    got = set(map(int, re.findall(r"\d+", got )))
    
    return len(winning.intersection(got))

cards = [1 for _ in data]

for i, line in enumerate(data):
    
    score = get_score(line)
    
    for y in range(i+1, i+1+score):
        cards[y] += cards[i]

print(sum(cards))
