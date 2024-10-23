from collections import defaultdict
import re 
from math import prod
from get_data import get_aoc_input

lines = get_aoc_input(2, 2023).splitlines()
given = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}


val = 0
powers = 0

for i, l in enumerate(lines, start = 1):
    
    start = l.find(":")
    
    cubes = defaultdict(lambda : 0)
    
    for s in re.split("; |, ", l[start + 1 :]):
        
        number, color = s.strip().split()
        cubes[color] = max(cubes[color], int(number))
    
    powers += prod(cubes.values())
    
    if all(given[key] >= val for key,val in cubes.items()):
        val += i
        
print(val, powers)