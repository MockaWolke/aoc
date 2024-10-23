import numpy as np

inputs = '''1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122'''.splitlines()

inputs = open("25.txt").read().splitlines()

s = 0

for n in inputs:
    val = 0
    for i,m in enumerate(n):
        
        if m.isnumeric():
            v = int(m)
        elif m=='-':
            v = -1
        else:
            v = -2
        
        val += 5**(len(n)-i-1) * v    
    # print(n,val)
    s += val
        
def get_potens(val):
    v = np.inf
    pot = 0
    
    while True:
        
        nv = abs(val - 5**pot)
        if nv > v:
            return pot-1
        v = nv
        pot +=1
        
def get_snafu(number):
    
    pot = get_potens(number)
    print('Potenz:',pot)
    rest = number
    s = ""
    for p in range(pot,-1,-1):
        
        factors = np.arange(-2,3)
        residuals = [np.abs(rest- ((5 ** p) * i)) for i in factors]
        factor = factors[np.argmin(residuals)]
        rest -= ((5 ** p) * factor)
        
        if factor==-1:
            s = s + "-"
        elif factor==-2:
            s = s + "="
        else: 
            s = s + str(factor)
    assert rest == 0, 'Oh Dear!'
    return s

print('Part 1:',get_snafu(s))