import numpy as np
import aocd
import sys
import time
start = time.time()

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush() 

s = aocd.get_data(day=19,year=2021)
s=[c.splitlines()[1:] for c in s.split("\n\n")]
s = [[eval(b) for b in d ] for d in s]

def hashes(scanner):
    h = []
    for i,b in enumerate(scanner):
        for y,d in enumerate(scanner):
            if i!=y:
                h.append(np.sqrt(((b-d)**2).sum()))
    return np.unique(h)

h_s = [hashes(np.array(b)) for b in s]

matches = {i:set() for i in range(len(s))}
for q,w in enumerate(h_s):
    for e,r in enumerate(h_s):
        if q!=e:
            if len(set(r).intersection(w))>=32:
                matches[q].add(e)
                matches[e].add(q)

def rotate_x_y(ar,d="xy"):
    if d=="xy":
        ar= ar[:,[1,0,2]]
        ar[:,0]*=-1    
    elif d=="xz":
        ar= ar[:,[2,1,0]]
        ar[:,0]*=-1    
    elif d[:2]=="yz":
        ar= ar[:,[0,2,1]]
        ar[:,2]*=-1 * (1-2*(d[2]=="1"))
        ar[:,1]*= (1-2*(d[2]=="1"))
    return ar

scanners = [np.array(b) for b in s]
scanner_pos = [(0,0,0)]


def rel_dis(scanner):
    h = []
    for i,b in enumerate(scanner):
        for o,d in enumerate(scanner):
            if i!=o:
                iii = np.add(d,b*-1)
                if np.abs(iii).max()<=3000:
                    h.append(iii.tolist())
    return h

def match(c):
    global crd
    ll = 0
    while ll<6:
        if ll<2:
            q = rotate_x_y(c,f"yz{ll+1}")
            for i in range(4):
                if len([True for b in rel_dis(q) if b in crd])>=66:
                    return q
                q = rotate_x_y(q)
        else:
            q = c
            for i in range(4):
                if len([True for b in rel_dis(q) if b in crd])>=66:
                    return q
                q = rotate_x_y(q)
            c = rotate_x_y(c,"xz")
        ll+=1

def get_scanner_pos(c,beacons):
    for b in beacons:
        r = [np.add(b,-1*np.array(c)).tolist() for c in beacons if b!=c]
        for q in c:
            if len([True for j in c if [q[0]-j[0],q[1]-j[1],q[2]-j[2]] in r])>=11:
                return [b[0]-q[0],b[1]-q[1],b[2]-q[2]]

center = scanners[0]
done = [0]
to_do = [(0,c) for c in matches[0]]
crd = rel_dis(center)
belongs_to = {0:[i for i in range(len(center))]}

for i in range(1,len(scanners)):
    belongs_to[i]=[]
while to_do:
    
    relevant, n = to_do.pop()

    beacons = center[belongs_to[relevant]]
    crd = rel_dis(beacons)
    c = scanners[n]
    nc = match(c)
    c_pos = get_scanner_pos(nc.tolist(),beacons.tolist())
    scanner_pos.append(c_pos)
    nc[:]+=c_pos
    for b in nc.tolist():
        STOP = False
        for pos,p in enumerate(center.tolist()):
            if b==p:
                belongs_to[n].append(pos)
                STOP = True
                break
        if STOP:
            continue
        belongs_to[n].append(len(center))
        center = np.concatenate((center,[b]))        
    done.append(n)
    for t in matches[n]:
        if t not in done and t not in [b for a,b in to_do]:
            to_do.append((n,t))
    progress(len(done),len(scanners),"Merging beacons")

print("\nPart 1", len(center))

k = 0
for n in scanner_pos:
    for j in scanner_pos:
        if n!=j:
            k = max(k,sum([abs(a-b) for a,b in zip(n,j)]))
print("Part 2",k)
print("Took ",time.time()-start)
