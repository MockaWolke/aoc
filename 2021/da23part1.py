import numpy as np
import heapq
import time
import aocd
import sys


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))


def generate_state(s):
    s=s.splitlines()
    s[3]+="##"
    s[3]=s[3].replace(" ","#")
    s[4]+="##"
    s=  np.array([[b for b in c] for c in s])[1:-1,1:-1]
    tiles = {}
    for x,e in enumerate(s[0]):
        tiles[(0,x)]=e
    for x in range(2,9,2):
        for y,e in enumerate(s[1:,x]):
            tiles[(y+1,x)]=e
    a=dict()
    c = np.zeros(4,dtype=int)
    for t in tiles:
        if tiles[t]!=".":
            a[tiles[t]+str(c[ord(tiles[t])-ord("A")])]=t
            c[ord(tiles[t])-ord("A")]+=1
    return tuple(tiles.items()),tuple(a.items())
state = generate_state(aocd.get_data(day=23,year=2021))

def passebal(x,nx,tiles):
    if nx>x:
        return all(["."==tiles[(0,c)] for c in range(x,nx+1)])
    elif x>nx:
        return all(["."==tiles[(0,c)] for c in range(nx,x+1)])
    else:
        return "."==tiles[(0,x)]

def next_states(cost,state):
    tiles,am = state
    tiles = dict(tiles)
    am = dict(am)
    floor_states = []
    good_moves = []
    
    for a in am:
        typ = a[0]
        goal = 2*(ord(typ)-ord("A")+1)
        y,x = am[a]
        c_cost = 0
        
        if y>0: #if we stand in column
            
                    
            if x!=goal or not all([typ==tiles[(q,x)] if len(range(y+1,3))>0 else True for q in range(y+1,3)]): # and we are in the wrong or not nicely stacked correct column
           
                    
                if y==1 or all(["."==tiles[(c,x)] for c in range(1,y)]):
                    c_cost+=y # we have to step out 
               

                    if goal!=x:
                        if passebal(x,goal,tiles)==1: 
                            cc_cost=c_cost + abs(goal-x) #we hae to go to the right column
                            goal_room = [tiles[(i,goal)] for i in range(1,3)]

                            if goal_room==[".",typ]:
                                good_moves.append((cc_cost+1,(a,1,goal)))
                            elif goal_room==[".","."]:
                                good_moves.append((cc_cost+2,(a,2,goal)))
 

                    if not(good_moves):
                        for nx in [0,1,3,5,7,9,10]:
                            if passebal(x,nx,tiles)==1:
                                floor_states.append((c_cost+abs(nx-x),(a,0,nx)))

                            
            else: #return new state without amphi in dict
                n_am = am.copy()
                n_am.pop(a)
                return [(0,((tuple(tiles.items())),(tuple(n_am.items()))))] # return as only state
            
        else: # we are in floor

            lx = x-1 if goal<x else x+1
            if passebal(lx,goal,tiles)==1: # if we can reach goal
                    cc_cost = c_cost + abs(goal-x)
                    goal_room = [tiles[(i,goal)] for i in range(1,3)]
                    if goal_room==[".",typ]:
                        good_moves.append((cc_cost+1,(a,1,goal)))
                    elif goal_room==[".","."]:
                        good_moves.append((cc_cost+2,(a,2,goal)))
 

    agg = []                
    if good_moves:

        for nc,ns in good_moves:
            a,ny,nx = ns
            y,x = am[a]
            n_am = am.copy()
            n_am.pop(a)
            n_tiles = tiles.copy()
            n_tiles[(y,x)]="."
            n_tiles[(ny,nx)]=a[0]
            nc*=10**(ord(a[0])-ord("A"))
            agg.append((nc+cost,((tuple(n_tiles.items())),(tuple(n_am.items())))))
    else:
        for nc,ns in floor_states:
            
            a,ny,nx = ns
            y,x = am[a]
 
            n_am = am.copy()
            n_am[a]=(ny,nx)
            n_tiles = tiles.copy()
            n_tiles[(y,x)]="."
            n_tiles[(ny,nx)]=a[0]

            nc*=10**(ord(a[0])-ord("A"))
            agg.append((nc+cost,((tuple(n_tiles.items())),(tuple(n_am.items())))))
    return agg


finish_state=  lambda s: len(s[1])==0

q = [(0,state)]
heapq.heapify(q)
z = time.time()
ben_there =set()
def run():
    while True:
        c,el = heapq.heappop(q)
        ben_there.add(el[1])
        if c%1000:
            progress(c,14000,"working")
        if finish_state(el):
            return c

        for cost,s in  next_states(c,el):
            if s[1] in ben_there:
                continue
            else:
                heapq.heappush(q,(cost,s))
myval = run()
print("\n",myval,time.time()-z)