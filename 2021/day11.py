import numpy as np
import aocd

s = np.array([[int(c) for c in b]for b in aocd.get_data(day=11,year=2021).splitlines()])


flashes = 0
def tick():
    global flashes
    global s
    s+=1
    mask = s>9
    old = s> 9
    while np.any(mask):
        for y,x in np.argwhere(mask):
            flashes+=1
            s[max(0,y-1):min(y+1,s.shape[0]-1)+1,max(0,x-1):min(x+1,s.shape[1]-1)+1]+=1
        mask = np.logical_xor(s>9,old)
        old = np.logical_or(mask,old)
    s[s>9]=0


i = 0
while not(np.all(s==0)):
    i+=1
    tick()
    if i==100:
        print(flashes)
print(i)





