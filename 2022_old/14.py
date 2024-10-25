lines = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()

lines = open('14.txt').read().splitlines()

cave = {(500,0):'+'}

for l in lines:

    it = l.split(" -> ")
    last_x,last_y = map(int,it[0].split(","))


    for pack in it[1:]:
        new_x,new_y = map(int,pack.split(","))
        if last_x==new_x:
            for y in range(min(new_y,last_y),max(new_y,last_y)+1):
                cave[(last_x,y)] = '#'

        elif last_y==new_y:
            for x in range(min(new_x,last_x),max(new_x,last_x)+1):
                cave[(x,last_y)] = '#'
        else:
            print("Diagonal input")

        last_x,last_y = new_x,new_y



def print_cave():
    x_cor = [i[0] for i in cave.keys()]
    y_cor = [i[1] for i in cave.keys()]

    for y in range(min(y_cor),max(y_cor)+1):

        s = "".join([cave[(x,y)] if (x,y) in cave else "." for x in range(min(x_cor)-1,max(x_cor)+1)])
        s = s + f"  {y}"
        print(s)

    print()
    # x_names = [str(x) for x in x_cor]

max_y = max([i[1] for i in cave.keys()])

def sand_fall():
    

    start = (500,0)
    x,y = start

    while True:

        if (x,y+1) not in cave and y+1<= max_y:
            x,y = x,y+1
        elif (x,y+1) not in cave and y+1> max_y:
            return False
        elif (x-1,y+1) not in cave:
            x,y = x-1,y+1
        elif (x+1,y+1) not in cave:
            x,y = x+1,y+1
        else:
            if (x,y) in cave:
                print("Error!!")
            cave[(x,y)] = 'o'
            return True
print_cave()    

steps = 0
while sand_fall():
    steps+=1


print_cave()

print("Part 1", steps)