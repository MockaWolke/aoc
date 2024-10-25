import re 
import heapq
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

lines = open("16.txt","r").read().splitlines()

valve = {}


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

# el_pos,my_pos, open_valves,el_ag,my_ag. time, amount of presure released   
state_0 =('AA','AA',tuple(),tuple(),tuple(),26,0)
states = [state_0]
finish_state = 0      

been_there = {}


def get_states(state):

    el_valve,my_valve, open_valves,el_ag,my_ag,time_left,presure_released = state

    time_left -= 1

    elefant_moves = []
    
    # if elefant wants to move some where
    if len(el_ag):
        elefant_moves.append((el_ag[0],my_valve, open_valves,el_ag[1:],my_ag,time_left,presure_released))
    
    # if not opened and important     
    elif el_valve in imp_val.difference(open_valves):
        
        new_set = tuple(sorted(open_valves + (el_valve,)))
        new_released = presure_released + time_left* flow_rates[el_valve]

        elefant_moves.append((el_valve,my_valve, new_set,el_ag,my_ag,time_left,new_released))

    else:
        my_goal = my_ag[-1:] if len(my_ag) else tuple()
        
        goals_left = imp_val.difference(open_valves + my_goal)
        if goals_left:
            for imp in goals_left:

                agenda = fastest_paths[el_valve,imp]
                elefant_moves.append((agenda[1],my_valve, open_valves,agenda[2:],my_ag,time_left,presure_released))
        else:
            elefant_moves.append((el_valve,my_valve, open_valves,el_ag,my_ag,time_left,presure_released))


    final_states = []

    for el_valve,my_valve, open_valves,el_ag,my_ag,time_left,presure_released in elefant_moves:
        
        # if i want to to get some where
        if len(my_ag):
            final_states.append((el_valve,my_ag[0], open_valves,el_ag,my_ag[1:],time_left,presure_released))
        
        # if not open_valves and important     
        elif my_valve in imp_val.difference(open_valves):
            
            new_set = tuple(sorted(open_valves + (my_valve,)))
            new_released = presure_released + time_left* flow_rates[my_valve]

            final_states.append((el_valve,my_valve, new_set,el_ag,my_ag,time_left,new_released))

        else:
            el_goal = el_ag[-1:] if len(el_ag) else tuple()

            goals_left = imp_val.difference(open_valves + el_goal)
            if goals_left:
                for imp in goals_left:


                    agenda = fastest_paths[my_valve,imp]
                    final_states.append((el_valve,agenda[1], open_valves,el_ag,agenda[2:],time_left,presure_released))

            else:
                final_states.append((el_valve,my_valve, open_valves,el_ag,my_ag,time_left,presure_released))

    return final_states


highest_presure = 0


while states:

    state = states.pop(0)

    if state[:-4] in been_there:

        time_left,presure_released = state[-2:]

        if state[-1] > presure_released and state[-2] <= time_left:
            continue
    else:

        been_there[state[:-4]] = state[-2:]


    if state[-1]>highest_presure:
        print("new val:",state[-1],"time :",state[-2], "len of states",len(states),"open",len(imp_val)-len(state[2]))
        
        highest_presure = state[-1]



    for next_state in get_states(state):

        time_left,presure_released = been_there.get(next_state[:-4],(26,0))
        
        if time_left > next_state[-2] and presure_released > next_state[-1]:

            continue

        if next_state[-2]<17 and next_state[-1]<700:
            continue
    
        if next_state[-2]<14 and next_state[-1]<1200:
            continue

        if next_state[-2]<13 and next_state[-1]<1350:
            continue

        if next_state[-2]<9 and next_state[-1]<1700:
            continue

        if next_state[-2]<4 and next_state[-1]<1950:
            continue

        if len(state[2]) == len(imp_val):
            continue


        states.append(next_state)


print("Part 2", highest_presure)
