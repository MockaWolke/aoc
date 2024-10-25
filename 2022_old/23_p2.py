lines = """..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
..............""".splitlines()
test = True

lines = open("23.txt").read().splitlines()
test = False


elves = {(y,x) for y,l in enumerate(lines) for x,c in enumerate(l) if c=='#'}

n_list = [(a,b) for a in [-1,0,1] for b in [-1,0,1] if (a,b)!=(0,0)]

add_tuple = lambda x,y: (x[0]+y[0],x[1]+y[1])

south = [(1,0),(1,1),(1,-1)], (1,0)
north = [(-1,0),(-1,1),(-1,-1)], (-1,0)
west = [(0,-1),(1,-1),(-1,-1)], (0,-1)
east = [(0,1),(1,1),(-1,1)], (0,1)
operation = [north,south,west,east]
order = ['n','s','w','e']

def move_at_all(cords,elves):
    for n in n_list:

        if add_tuple(n,cords) in elves:
            return True

    return False


def step(elves,intructions):
    new_elves = set()
    go_there = {}

    for elve in elves:

        if not move_at_all(elve,elves):
            new_elves.add(elve)

            continue

        for ins,target in intructions:
            
            val = any(add_tuple(elve,i) in elves for i in ins)

            if not val:
                t = add_tuple(elve,target)
                if t in go_there:
                    go_there[t].append(elve)
                
                else:
                    go_there[t] = [elve]

                break

        else:
            new_elves.add(elve)


    for target, elvies in go_there.items():
        if len(elvies)==1:
            new_elves.add(target)

        else:
            new_elves = new_elves.union(elvies)

    return new_elves, len(go_there) == 0


def get_regtangle(elves):
    ys = [i[0] for i in elves]
    xs = [i[1] for i in elves]

    return min(ys), max(ys), min(xs), max(xs)

def print_field(elves):

    y_min,y_max , x_min,x_max = get_regtangle(elves)
    
    for y in range(y_min,y_max+1):
        
        s = "".join(["#" if (y,x) in elves else "." for x in range(x_min,x_max+1)])
        print(s)

    print("\n\n")
        
if test:
    print_field(elves)

i = 1

while True:

    new_elves,stop_criteroium = step(elves,operation)

    if stop_criteroium:
        break

    elves = new_elves
    
    if test:
        print(f"Round {i}:")
        print("Order: ",order)
        print_field(elves)


    i+=1
    operation = operation[1:] + operation[:1]
    order = order[1:] + order[:1]


print("Part 2:",i)