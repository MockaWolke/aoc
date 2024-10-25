from aoc.get_data import get_aoc_input

data = get_aoc_input(day = 3, year= 2023).splitlines()

symbols = set()

for y,line in enumerate(data):
    for x, char in enumerate(line):
        if not (char.isdigit() or char == "."):
            symbols.add((y,x))
            
            
numbers = 0
            
def parse_number(y,line, x):
    global numbers
    start = x-1
    
    while x < len(line) and (char := line[x]).isdigit():
        x+=1
        
    end = x
    
    number = int(line[start +1 : end])
    
    special = False
    
    for y_diff in [-1, 0, 1]:
        for x_cor in range(start, end +1):
            
            if (y_diff + y, x_cor) in symbols:
                special = True
    
    if special:
        numbers += number
        
    return x
            
for y,line in enumerate(data):
    
    x = 0
    while x < len(line):
        
        if line[x].isdigit():
            x = parse_number(y, line, x)
        else:
            x += 1
    
print(numbers)