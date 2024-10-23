import aocd 
import re
import numpy as np
import time

t = time.time()

data =  [(b[1]=='n',[int(c) for c in re.findall(r'-?\d+',b)]) for b in aocd.get_data(day=22,year=2021).splitlines()]


overlap = lambda a,b : all([any([a[2*i]<=c<=a[2*i+1] for c in b[2*i:2*i+2]]) or any([b[2*i]<=c<=b[2*i+1] for c in a[2*i:2*i+2]]) for i in range(3)])

distinct =0
for i,d in enumerate(data):
    if d[0]==1:
        distinct = [d[1]]
        data = data[i+1:]
        break

def delete(dcubes, cube):
    n = []
    for d in dcubes:
        if overlap(d,cube):
            cuts = [max(d[i],cube[i]) if i%2==0 else min(d[i],cube[i]) for i in range(6)]
            if d[0]!=cuts[0]:
                n.append([d[0],cuts[0]-1]+d[2:])
            if d[1]!=cuts[1]:
                n.append([cuts[1]+1,d[1]]+d[2:])    
            if d[2]!=cuts[2]:
                n.append(cuts[:2]+[d[2],cuts[2]-1]+d[4:])
            if d[3]!=cuts[3]:
                n.append(cuts[:2]+[cuts[3]+1,d[3]]+d[4:])
            if d[4]!=cuts[4]:
                n.append(cuts[:4]+[d[4],cuts[4]-1])
            if d[5]!=cuts[5]:
                n.append(cuts[:4]+[cuts[5]+1,d[5]])
        else:
            n.append(d)
    return n

def print_counts():
    count = 0
    for d in distinct:
        count+=np.prod([d[i*2+1]+1-d[i*2] for i in range(3)])
    print(count)

outside_part_one_bounds = 0
for on,cube in data:
    if not(outside_part_one_bounds) and max(np.abs(cube))>0:
        print("Part 1")
        print_counts()
        outside_part_one_bounds=1
    
    distinct = delete(distinct,cube)
    if on:
        distinct.append(cube)
        
print("Part 2")
print_counts()

print("Took",time.time()-t,"s")
