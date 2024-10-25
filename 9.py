from aoc.get_data import get_aoc_input

data = get_aoc_input(9, 2023)

diff = lambda x: [x[i +1] - x[i] for i in range(len(x) - 1)]
is_zero = lambda x: all(i == 0 for i in x)

def extrapolate_values(d):
    d = list(map(int,d.split()))
    stack = [d]
    while not is_zero(l := stack[-1]):
        
        stack.append(diff(l))

    stack[-1].append(0)

    for i in range(1, len(stack)):
        
        cur = stack[-(i+1)]
        cur.append(cur[-1] + stack[-(i)][-1])
    
    return stack[0][-1]



def extrapolate_values2(d):
    d = list(map(int,d.split()))
    stack = [d]
    while not is_zero(l := stack[-1]):
        
        stack.append(diff(l))


    stack[-1].insert(0, 0)

    for i in range(1, len(stack)):
        
        cur = stack[-(i+1)]
        cur.insert(0, cur[0] - stack[-(i)][0])
    
    return stack[0][0]



val = sum(extrapolate_values(i) for i in data.splitlines())
val2 = sum(extrapolate_values2(i) for i in data.splitlines())
print(val, val2)