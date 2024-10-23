import re
import argparse

test = True


lines = open('19.txt').read().splitlines()

if test:
    lines = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.""".splitlines()

blueprints = []

get_ints = lambda l: list(map(int,re.findall("\d+",l)))

for l in lines:
    bp = {}
    l = l[l.find(":")+1:-1].split(".")
    bp['ore'] = get_ints(l[0])[0]
    bp['clay'] = get_ints(l[1])[0]
    bp['obisian'] = tuple(get_ints(l[2]))
    bp['geode'] = tuple(get_ints(l[3]))
    blueprints.append(bp)
print(blueprints)

# filter out minima

def filter_out_not_imp():
    pass


# state presentations 
# resources = (ore,clay,obsidian,geodes)
# robots = (ore,clay,obsidian,geodes)
# state = (resources, robots,time)

def can_buy(bp,resources,robots,time):
    
    res = [(resources,robots)]

    if resources[0] >= bp['ore']:
        res.append(((resources[0]-bp['ore'],) + resources[1:], (robots[0]+1,) + robots[1:]))
    
    if resources[0]>= bp['clay']:
        res.append(((resources[0]-bp['clay'],resources[1]) + resources[2:], (robots[0],robots[1]+1,) + robots[2:]))

    obs_ore,obs_clay = bp['obisian']

    if resources[0] >= obs_ore and resources[1] >= obs_clay:

        res.append(((resources[0]-obs_ore,resources[1]-obs_clay) + resources[2:], robots[:2] + (robots[2]+1,robots[3])))

    geode_ore,geode_obs = bp['geode']

    if resources[0] >= geode_ore and resources[2] >= geode_obs:

        res.append(((resources[0]-geode_ore,resources[1],resources[2]-geode_obs,resources[3]) , robots[:3]+ (robots[3]+1,)))

    return res

def process_state(bp,state):
    next_states = []

    resources, robots,time = state
    new_time = time  + 1

    for new_resourses,new_robots in can_buy(bp,resources,robots,time):
        new_resourses = tuple(i+b for i,b in zip(new_resourses,robots))
        next_states.append((new_resourses,new_robots,new_time))

    return next_states

start = ((0,0,0,0),(1,0,0,0),0)
states = [start]

max_val = 0
been_threre = set()
bp = blueprints[1]

while states:
    
    state = states.pop(0)
    # print(state,len(states))    
    if state[:2] in been_threre or state[2]==25:
        continue
    
    been_threre.add(state[:2])

    og_max_val = max_val
    max_val = max(max_val,state[0][-1])
    if og_max_val!= max_val:
        print("new val:",max_val,"state :",state,len(states)) 

    for next_state in process_state(bp,state):

        if next_state[:2] in been_threre:
            continue

        # if next_state[-1] > 20 and next_state[1][-1]==0:
        #     continue
        states.append(next_state)   
