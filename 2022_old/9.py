lines = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()

lines = open("9.txt").read().splitlines()

from aocd import get_data
lines = get_data(day=9,year=2022).splitlines()  

head = (0,0)
tail = (0,0)
been_there = {tail:True}


for l in lines:
    dir, times = l.split(" ")

    for i in range(int(times)):
        last_head_pos = head

        match  dir:
            case 'R':
                head = (head[0]+1,head[1])
            case 'U':
                head = (head[0],head[1]+1)
                
            case 'D':
                head = (head[0],head[1]-1)
                
            case 'L':
                head = (head[0]-1,head[1])

        x_diff = abs(head[0]-tail[0])
        y_diff = abs(head[1]-tail[1])

        if x_diff + y_diff == 1:
            tail = last_head_pos

        elif x_diff + y_diff == 2:
            tail = last_head_pos


        been_there[tail] = True




print(len(been_there))