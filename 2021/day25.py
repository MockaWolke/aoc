import numpy as np
import aocd
i = aocd.get_data(day=25,year=2021).splitlines()
f=np.array([[ord(c)-ord(".") for c in v]for v in i],dtype=int)//16

shape = f.shape

def tick(f):
    change = False
    c = f.copy()
    for y,x in np.argwhere(f==1):
        k = (x+1)%shape[1]
        if f[y,k]==0:
            change = True
            c[y,x]=0
            c[y,k]=1

    f = c.copy()
    for y,x in np.argwhere(c==4):
        k = (y+1)%shape[0] 
        if c[k,x]==0:
            change = True
            f[y,x]=0
            f[k,x]=4
    
    return f,change


v = True
i = 0
while v:
    f,v=tick(f)
    i+=1
print(i)

