import numpy as np
import aocd
import heapq



s = aocd.get_data(day=15,year=2021).splitlines()
s = np.array([[int(c) for c in b]for b in s])




def neighbor(y,x):
    return [(q,e) for q,e in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)] if 0<=q<s.shape[0] and 0<=e<s.shape[1]]



def search():
    q = [(0,(0,0))]
    been_there = np.zeros(s.shape)
    heapq.heapify(q)
    while True:
        cost, e = heapq.heappop(q)
        y,x = e
        if (y+1,x+1)==s.shape:
            return cost
        if been_there[y,x]==0:
            been_there[y,x]=1
            for z,d in neighbor(y,x):
                heapq.heappush(q,(cost+s[z,d],(z,d)))



print(search())




c = s.copy()
for _ in range(4):
    c+=1
    c[c>9]=1
    s = np.concatenate((s,c),axis=0)
b = s.copy()
for _ in range(4):
    b+=1
    b[b>9]=1
    s = np.concatenate((s,b),axis=1)
print(search())

