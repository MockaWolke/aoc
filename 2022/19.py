import re
from collections import deque
import numpy as np

TEST = False

if TEST:

    inputs = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.""".splitlines()

else: 
    inputs = open('19.txt').read().splitlines()

get_ints = lambda x: [int(c) for c in re.findall(r"\d+", x)]

names = ["id", "ore", "clay", "obs", "geode"]

blueprints = []


for b in inputs:

    vals = [get_ints(i) for i in b[:-1].replace(":", ".").split(".")]

    blueprints.append(dict(zip(names, vals)))

# filter out worse

def filter_out(blueprints):
    
    ars = [np.array(list(bp.values())[1:]) for bp in blueprints]
    
    new_bps = []
     
    for i,bp in enumerate(blueprints):
        
        others = np.array(ars[:i] + ars[i + 1:])
        
        val = (others < ars[i]).all(1)
        better = np.argmax(val)
        val = val.any()
        
        if val:
            print('Drop bp number:',bp['id'],'Better:',blueprints[better]['id'])
        else:
            new_bps.append(bp)
            
    print('Blueprints reduced. From :',len(blueprints),'To:',len(new_bps))
            
    return new_bps
        
        
# blueprints = filter_out(blueprints)


# state
# time, ore, clay,obs,geode, ore_rob, clay_rob,obs_rob,geode_rob,
start_state = (0, (0, 0, 0, 0), (1, 0, 0, 0))


def can_buy(resources, bp):

    resources = list(resources)
    states = []

    if resources[0] >= bp["ore"][0]:

        new_res = resources.copy()
        new_res[0] -= bp["ore"][0]
        states.append((tuple(new_res), (1, 0, 0, 0)))

    if resources[0] >= bp["clay"][0]:

        new_res = resources.copy()
        new_res[0] -= bp["clay"][0]
        states.append((tuple(new_res), (0, 1, 0, 0)))

    if resources[0] >= bp["obs"][0] and resources[1] >= bp["obs"][1]:

        new_res = resources.copy()
        new_res[0] -= bp["obs"][0]
        new_res[1] -= bp["obs"][1]

        states.append((tuple(new_res), (0, 0, 1, 0)))

    if resources[0] >= bp["geode"][0] and resources[2] >= bp["geode"][1]:

        new_res = resources.copy()
        new_res[0] -= bp["geode"][0]
        new_res[2] -= bp["geode"][1]

        states.append((tuple(new_res), (0, 0, 0, 1)))

    return states


def process_step(state, bp, collecter, set_col,current_max):

    if state[1:] in set_col:
        return

    set_col.add(state[1:])

    time, resourses, robots = state

    time += 1

    next_states = [(tuple(resourses), (0, 0, 0, 0))]
    if time!= 24:
        next_states.extend(can_buy(resourses, bp))

    for state in next_states:

        processed_res, ad_robs = state

        new_recourses = tuple(sum(a) for a in zip(processed_res, robots))
        new_robs = tuple(sum(a) for a in zip(ad_robs, robots))

        new_state = (time, new_recourses, new_robs)

        if new_state[1:] in set_col:
            continue

        if time >= 20:
            curent_val = new_recourses[-1]

            if curent_val + robots[-1] * 2 + (24 - time)*2 < current_max:
                continue

        collecter.append(new_state)


def find_best_res(bp):

    name = bp['id'][0]
    print('-'*15,'Now:',name,'-'*15 )

    collecter = deque([start_state])
    i = 0
    been_there = set()
    max_geode = 0

    while collecter:

        state = collecter.popleft()

        geode_count = state[1][-1]
        time = state[0]

        if geode_count > max_geode:

            print("New Max",name, state)
            max_geode = geode_count

        if time < 24:
            process_step(state, bp, collecter, been_there,max_geode)

        i += 1
            
    res = max_geode * name
    print('-'*15,name,'Result:',res,'-'*15 )
            
            
    return res



def main():
    
    print([bp['id'] for bp in blueprints])
    
    res = sum(find_best_res(bp) for bp in blueprints)

        
        
    return res

if __name__ == '__main__':

    print("Part 1:", main())