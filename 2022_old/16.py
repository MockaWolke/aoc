import re 
import heapq

# import heapq
lines = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".splitlines()

# lines = open("16.txt","r").read().splitlines()

neighbors = {}
flow_rates = {}


for l in lines:

    flow_rate = int(re.findall(r'\d+',l)[0])
    name = l.split()[1]
    connects_to = tuple([i.replace(",","") for i in l.split()[9:]])
    neighbors[name] = connects_to
    flow_rates[name] = flow_rate


def djikstra(start,goal):

    been_there = set()
    q = [(0,(start,(start,)))]
    heapq.heapify(q)

    while q:

        cost,(valve,path) = heapq.heappop(q)
        print(cost,valve,path)

        if been_there in been_there:
            continue

        been_there.add(valve)

        if valve==goal:
            return path

        for n in neighbors[valve]:

            if n not in been_there:
                heapq.heappush(q,(cost +1 ,(n,path+(n,))))


imp_val = {i for i,a in flow_rates.items() if a > 0}
fastest_paths = {}

for v1 in imp_val:

    fastest_paths[('AA',v1)] = djikstra('AA',v1)

    for v2 in imp_val:

        if v1!=v2:
            fastest_paths[(v1,v2)] = djikstra(v1,v2)
print(djikstra('AA','JJ'))


# print(fastest_paths)
exit()






state_0 =('AA',tuple(),30,0)
states = [state_0]
finish_state = 0






been_there = {}


while states:
    state = states.pop()
    # print(state)
    current,opened,time_left,released = state
    if len(opened) ==0 and time_left<20:
        continue
    if state[:-1] not in been_there:
        been_there[state[:-2]] = (time_left,released)
    else:
        val = been_there[state[:-1]]
        if val[1] > released and time_left<=val[0]:
            continue
        val = (time_left,released)


    if time_left == 0:
        finish_state = max(released,finish_state)
        # if finish_state==released:
        #     print('finished with',finish_state,len(states))
        continue

    time_left -= 1
    if valve[current][0] != 0 and current not in opened:
        new_set = tuple(sorted(opened + (current,)))
        new_released = released + time_left* valve[current][0]

        dict_val = been_there.get((current,new_set),(30,0))
        if dict_val[1]<new_released or (dict_val[1]==new_released and dict_val[0]<=time_left):
            states.append((current,new_set,time_left,new_released))

    for n in valve[current][1]:
        
        dict_val = been_there.get((n,opened),(30,-1))
        # print(dict_val,time_left,released)
        if dict_val[1]<released or (dict_val[1]==released and dict_val[0]<=time_left):
            states.append((n,opened,time_left,released))
        


print("part 1:",finish_state)

