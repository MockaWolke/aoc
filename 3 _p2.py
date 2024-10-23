from get_data import get_aoc_input
from math import prod

data = get_aoc_input(day = 3, year= 2023).splitlines()

symbols = dict()

for y,line in enumerate(data):
    for x, char in enumerate(line):
        if not (char.isdigit() or char == "."):
            symbols[(y,x)] = []
            
            
            
def parse_number(y,line, x):
    global numbers, symbols
    start = x-1
    
    while x < len(line) and (char := line[x]).isdigit():
        x+=1
        
    end = x
    
    number = int(line[start +1 : end])
    
    special = False
    
    for y_diff in [-1, 0, 1]:
        for x_cor in range(start, end +1):
            
            if (y_diff + y, x_cor) in symbols:
                symbols[(y_diff + y, x_cor)].append(number)
                special = True
    
    return x
            
for y,line in enumerate(data):
    
    x = 0
    while x < len(line):
        
        if line[x].isdigit():
            x = parse_number(y, line, x)
        else:
            x += 1
    

number = sum(prod(i) for i in symbols.values() if len(i) == 2)
    
print(number)