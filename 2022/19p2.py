import re
from collections import deque
import numpy as np
from math import prod

TEST = False
END = 32

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
    if time!= END:
        next_states.extend(can_buy(resourses, bp))

    for state in next_states:

        processed_res, ad_robs = state

        new_recourses = tuple(sum(a) for a in zip(processed_res, robots))
        new_robs = tuple(sum(a) for a in zip(ad_robs, robots))

        new_state = (time, new_recourses, new_robs)

        if new_state[1:] in set_col:
            continue

        curent_val = new_recourses[-1]

        t_left = (END - time)

        if curent_val + t_left * (robots[-1] + (t_left + 1)/2) < current_max:
            continue

        collecter.append(new_state)


def time_reg(time): 
    time_left = END - time
    
    return int(time_left * (time_left +1 )/2)


def project_max(state,bp,v = True):
    time, resourses, robots = state
    
    while time != END:
        time +=1
        
        
        resourses = list(resourses)
        
        if resourses[0] >= bp["geode"][0] and resourses[2] >= bp["geode"][1]:

            resourses[0] -= bp["geode"][0]
            resourses[2] -= bp["geode"][1]
            new_rob = tuple(sum(a) for a in zip(robots,(0,0,0,1)))
            
        else:
            new_rob = robots 
        
        resourses = tuple(sum(a) for a in zip(robots,resourses))
        
        robots = new_rob

    proj = resourses[-1]
    
    time_r = 0
    for i in range(state[0],END):
        if time_reg(i) < proj:
            time_r = i
            break
            
    if v: print('Minimum projected Result:',proj,'Time',state[0],'Works at',time_r)
    
    return proj,time_r



def find_best_res(bp):

    name = bp['id'][0]
    print('-'*15,'Now:',name,'-'*15 )

    collecter = deque([start_state])
    i = 0
    been_there = set()
    max_geode = 0

    first_rob = False
    c_time = 0
    work_at = END
    c_max = 0

    while collecter:

        state = collecter.popleft()

        time = state[0]

        if c_time< time:

            time_sum = time_reg(time)
            print('Reached time',time,'Time sum',time_sum, len(collecter),len(been_there))
            c_time = time

        if (not first_rob )and state[2][-1]:
            max_geode, work_at = project_max(state,bp)
            
            time_sum = time_reg(time)

            
            first_rob = True
            

        geode_count = state[1][-1]
        time = time

        if geode_count > c_max:
            c_max = geode_count
            n_max_geode, n_work_at = project_max(state,bp,v=False)
            if n_max_geode > max_geode:
                print('New:',n_max_geode,'old',max_geode,'works at:',n_work_at)
                max_geode, work_at = n_max_geode, n_work_at
            

        if time < END:
            
            if time < work_at:
    
                process_step(state, bp, collecter, been_there,max_geode)
                
                continue
            
            t_left = (END - time)

            if geode_count + t_left * (state[2][-1] + (t_left + 1)/2) < max_geode:
                continue
            
            process_step(state, bp, collecter, been_there,max_geode)
                

            
            
    res = max_geode
    print('-'*15,name,'Result:',res,'-'*15 )
            
    return res



if __name__ == '__main__':

    print([bp['id'] for bp in blueprints])
    
    blueprints = blueprints[:3]
    
    res = prod(find_best_res(bp) for bp in blueprints)

    print("Part 2:", res)