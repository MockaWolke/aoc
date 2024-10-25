import re
import heapq

lines= """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".splitlines()

lines = open('16.txt').read().splitlines()

valves = {}
imp = set()

for l in lines:
    name = l.split(" ")[1]
    flow_rate = int(re.findall(r'\d+',l)[0])
    leads_to = re.search(r'([A-Z]+, )*[A-Z]+$',l).group(0).replace(",","").split(" ")

    valves[name] = (flow_rate,tuple(leads_to))
    if flow_rate > 0:
        imp.add(name)

def find_shortest_path(imp1,imp2):

    q = [(0,(imp1,tuple()))]
    heapq.heapify(q)
    been_there = set()

    while q:
        cost,(valve,path) = heapq.heappop(q)

        if  valve in been_there:
            continue

        been_there.add(valve)

        if valve==imp2:
            return path

        cost+=1

        for n in valves[valve][1]:
            if n not in been_there:
                heapq.heappush(q,(cost,(n,path + (n,))))

fastest_paths = {}
for a in imp.union(('AA',)):
    for b in imp:
        if a!=b:
            fastest_paths[(a,b)]= find_shortest_path(a,b)


#state = (released,(pos,opened,path,time))

q = [(0,('AA',tuple(),tuple(),30))]
been_threre  = {}
heapq.heapify(q)

highest = 0

while q:

    released, (pos,opened,path,time) = heapq.heappop(q)

    if (pos,opened) in been_threre:
        time_before,released_before = been_threre[(pos,opened)]
        if released_before < released and time_before >= time:
            continue

    been_threre[(pos,opened)] = (time,released)

    if -released==1647:
        break

    highest = max(highest,-released)

    time -= 1
 
    if len(path):
        heapq.heappush(q,(released,(path[0],opened,path[1:],time)))
        continue

    if pos in imp.difference(opened):
        new_opened = tuple(sorted(opened + (pos,)))
        new_released = released - time * valves[pos][0]
        # print(f"Opening {pos} at time {time-1}, flow rate {valves[pos][0]}. before {released} now {new_released}, {len(imp)-len(opened)}")
        heapq.heappush(q,(new_released,(pos,new_opened,path,time)))
        continue

    for left in imp.difference(opened + (pos,)):
        
        f_path = fastest_paths[(pos,left)]

        next_step = f_path[0]
        path_left = f_path[1:]

        heapq.heappush(q,(released,(next_step,opened,path_left,time)))


print("Part 1:", highest)
