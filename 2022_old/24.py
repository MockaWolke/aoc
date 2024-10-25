import heapq

lines = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#""".splitlines()
test = True

lines = open("24.txt").read().splitlines()
test = False

x_len = len(lines[0])-2
y_len = len(lines)-2

global_start = (-1,0)
global_goal = y_len,x_len-1

tornados = [((y,x),d) for y,l in enumerate(lines[1:-1]) for x,d in enumerate(l[1:-1]) if d!='.']
blocked = set([i[0] for i in tornados])

def move_tornardos(tornados):
    new_tornados = []
    blocked = set()

    for  tor in tornados:
        
        pos,typ = tor
        y,x = pos

        if typ == ">":
            pos = y,(x+1)%(x_len)
        elif typ == "<":
            pos = y,(x-1)%(x_len)
        elif typ == "v":
            pos = (y+1)%(y_len),x
        else:
            pos = (y-1)%(y_len),x
        
        new_tornados.append( (pos,typ))
        blocked.add(pos)
    
    return new_tornados,blocked


def print_field(tornados,current_pos):

    tors = {}
    for pos,typ in tornados:
        if pos in tors:
            tors[pos].append(typ)
        else:
            tors[pos] = [typ]

    print(lines[0])
    for y in range(y_len):
        s = '#'
        for x in range(x_len):

            if (y,x) == current_pos:
                s = s + "E"
                continue

            if (y,x) not in tors:
                s = s + "."
                continue
            
            i = tors[(y,x)]
            s  = s + str(len(i)) if len(i)>1 else s + i[0]
        
        s = s + '#'
        print(s)
    print(lines[-1])
    print("\n\n")



def step_cords(pos,blocked,start,goal):

    if start == (-1,0):
        after_start = (0,0)
        before_goal = (y_len-1,x_len-1)
    else: 
        after_start = (y_len-1,x_len-1)
        before_goal = (0,0)


    if pos == start and after_start not in blocked:
        
        return [after_start,start]

    if pos == start and after_start in blocked:
        return [start]

    if pos == before_goal:
        return [goal]

    next_pos = []

    # wait
    if pos not in blocked:
        next_pos.append(pos)

    y,x = pos

    for n in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:

        if not (-1 < n[0] < y_len and -1 < n[1] < x_len):
            continue

        if n in blocked:
            continue
        
        next_pos.append(n)

    return next_pos 


def search(start_time_point,start,goal,start_tornados,start_blocked):


    map_state = {start_time_point:(start_tornados,start_blocked)}
    if test:
        print("Start:")
        print_field(start_tornados,start)

    q = [(start_time_point,start)]
    heapq.heapify(q)
    been_there = set()


    while q:
        val = heapq.heappop(q)
        

        if val in been_there:
            continue

        been_there.add(val)

        (steps,pos) =  val

        if pos == goal:
            return steps, map_state[steps]

        steps +=1


        if steps not in map_state:
            map_state[steps] = move_tornardos(map_state[steps-1][0])
            print(f"Reached Step: {steps}, Pos: {pos}")
            if test:
                print_field(map_state[steps][0],pos)


        blocked = map_state[steps][1]



        for next_pos in step_cords(pos,blocked,start,goal):

            state = steps,next_pos
            
            if state in been_there:
                continue
            
            heapq.heappush(q,state)


time_to_goal,(tornados,blocked )= search(0,global_start,global_goal,tornados,blocked)
time_back_to_start,(tornados,blocked) = search(time_to_goal,global_goal,global_start,tornados,blocked)
time_back_to_goal,(tornados,blocked) = search(time_back_to_start,global_start,global_goal,tornados,blocked)



print(time_to_goal,time_back_to_start,time_back_to_goal)