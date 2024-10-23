import aocd
import numpy as np
s= aocd.get_data(day=9,year=2021).splitlines()
s = np.array([[int(c) for c in b] for b in s])

def neighbor(y,x,without=False):
    a = []
    for q,e in [(y+1,x),(y-1,x),(y,x-1),(y,x+1)]:
        if 0<=q<s.shape[0] and 0<=e<s.shape[1] and (q,e)!=without:
            a.append(s[q,e])
    return a

b = 0
mask = np.zeros(s.shape)
for y in range(s.shape[0]):
    for x in range(s.shape[1]):
        if s[y,x] < min(neighbor(y,x)):
            mask[y,x]=1
            b+=s[y,x]+1
print(b)

classy = np.zeros(s.shape)

def recur(y,x,c,direct):
    v = s[y,x]
    if v==9:
        return
    if direct:
        if not(s[direct] <= min(neighbor(y,x,direct))):
            return 
    classy[y,x]=c
    #part where others are checked
    for q,e in [(y+1,x),(y-1,x),(y,x-1),(y,x+1)]:
        if 0<=q<s.shape[0] and 0<=e<s.shape[1] and (q,e)!=direct:
            recur(q,e,c,(y,x))

nclass = 1
for y,x in np.argwhere(mask):
    recur(y,x,nclass,False)
    nclass+=1

_,h = np.unique(classy[classy>0],return_counts=1)
h.sort()
print(np.prod(h[-3:]))