import aocd
d = [i.split("-") for i in  aocd.get_data(day=12,year=2021).splitlines() ]
paths = {q:[] for b in d for q in b   }
for a,b in d:
    paths[a].append(b)
    paths[b].append(a)
start ={q:0 for b in d for q in b if q.islower()}
start["stop"]=0

#part 1
count = 0
def recur1(state,n):
    global count
    n_state = state.copy()
    if n=="end":
        count+=1
        return
    if n.islower():
        n_state[n]+=1

    for b in paths[n]:
        if b!="start":
            if b.isupper() or n_state[b]==0:
                recur1(n_state,b)
recur1(start,"start")
print("Part1" , count)


count = 0
def recur2(state,n):
    global count
    n_state = state.copy()
    if n=="end":
        count+=1
        return
    if n.islower():
        n_state[n]+=1
        n_state["stop"]= max(n_state[n]==2,n_state["stop"])
    
    for b in paths[n]:
        if b!="start":
            if b.isupper() or n_state[b]==0 or (n_state[b]==1 and n_state["stop"]==0):
                recur2(n_state,b)


recur2(start,"start")
print("Part2" ,count)
