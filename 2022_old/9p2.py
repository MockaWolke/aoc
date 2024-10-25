lines = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""".splitlines()

# lines = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2""".splitlines()

from aocd import get_data
lines = get_data(day=9,year=2022).splitlines()  
lines = open("9.txt").read().splitlines()


RADIUS = 15

# lines = open("9.txt").read().splitlines()

head = (0,0)


tails = [(0,0) for i in range(9)]

been_there = [set((0,0)) for i in range(9)]


def dir2cor(head,dir):

    match  dir:
        case 'R':
            return (head[0]+1,head[1])
        case 'U':
            return (head[0],head[1]+1)
            
        case 'D':
            return (head[0],head[1]-1)
            
        case 'L':
            return (head[0]-1,head[1])

def must_move(head,tail):

    x_diff = abs(head[0]-tail[0])
    y_diff = abs(head[1]-tail[1])

    return x_diff > 1 or y_diff > 1




# step 
def one_step(dir):
    global head, been_there, last_head_pos

    last_rel_head_pos = [head if i==0 else tails[i-1] for i in range(9)]


    # move head
    head = dir2cor(head,dir)

    # current_head = head

    # for every tail
    for i in range(9):
        current_head = head if i==0 else tails[i-1]

        current_tail = tails[i]

        # if no move then everything is okay
        m = must_move(current_head,current_tail)
        # print(i,i-1,m,current_head==tails[i-1])
        if not m:
            break

        # we must move

        current_last_real_head = last_rel_head_pos[i]
        # check if head before did diagonal jump

        # check if we are in the same row/column

        # we are in the same -> move up
        if (current_head[0]!=current_tail[0]) and (current_head[1]!=current_tail[1]):
            x_offset = 1 if current_head[0]>current_tail[0] else -1
            y_offset = 1 if current_head[1]>current_tail[1] else -1

            if x_offset + y_offset > 3:
                print("wtf")

            current_tail = (current_tail[0] + x_offset, current_tail[1]+y_offset)

        else:  # we must jump diagonal

            # print(current_head,current_tail)

            

            if (current_head[0]!=current_tail[0]):

                x_offset = 1 if current_head[0]>current_tail[0] else -1
                current_tail = (current_tail[0] + x_offset, current_tail[1])

            else:

                y_offset = 1 if current_head[1]>current_tail[1] else -1
                current_tail = (current_tail[0] , current_tail[1]+ y_offset)

            # current_tail = current_last_real_head
            # print('straight')




        # save pos
        # update
        tails[i] = current_tail
        been_there[i].add(current_tail)

        # for next tail

        # current_head = current_tail






def print_field(radius:int) -> str:

    global head, tails

    lines = ""

    for k,y in enumerate(range(radius,-radius,-1)):

        for x in range(-radius,radius):

            cords = (x,y)

            if (0,0)==cords:
                lines = lines + 's'
                continue


            if head==cords:
                lines = lines + 'h'
                continue

            stop = False
            for i in range(9):

                if tails[i]==cords:
                    lines = lines + str(i+1)
                    stop = True
                    break

            if stop: continue

            lines = lines + "."

        if k==0:
            lines = lines + f"   h: {head}"


        if k-1>0 and k%2==0:
            i = int(k/2)
            if i<10:
                lines = lines + f"   {i}: {tails[i-1]}"

        lines = lines + "\n"

                
    return lines

print(print_field(5))


def print_hits(radius):

    global been_there

    a = been_there[-1]

    lines = ""

    for y in range(radius,-radius,-1):

        for x in range(-radius,radius):

            cords = (x,y)

            if (0,0)==cords:
                lines = lines + 's'
            
            elif cords in a:
            
                lines = lines + '#'
                
            else:
                lines = lines + "."

        lines = lines + "\n"

                
    return lines


with open("9_p2_vis.txt","w") as f:

    # f.write(print_field(15)+"\n")

    for l in lines:
        dir, times = l.split(" ")

        for i in range(int(times)):
 
            # f.write(f"Dir: {dir}, Step: {i+1} \n")
            # print(dir,i+1)
            one_step(dir)

         
            # f.write(print_field(RADIUS)+"\n")

    # f.write(("\n\n"))
    # f.write(print_hits(RADIUS))

print(len(been_there[0]))

print(len(been_there[-1]))