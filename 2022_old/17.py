import tqdm
waves = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
waves = open('17.txt').read()

waves = [i==">" for i in waves]

stones = []
# stone 1
stones.append(lambda x,y: [(x+i,y) for i in range(4)])
# stone 2
stones.append(lambda x,y: [(x+i,y+1) for i in range(3)] + [(x+1,y),(x+1,y+2)])
#stone 3
stones.append(lambda x,y: [(x+i,y) for i in range(3)] + [(x+2,y+1),(x+2,y+2)])
#stone 4
stones.append(lambda x,y: [(x,y+i) for i in range(4)])
# stone 5
stones.append(lambda x,y: [(x,y+1),(x+1,y+1),(x,y),(x+1,y)])

rocks = {(i,0):'-' for i in range(7)}

get_max_y = lambda : max(i[1] for i in rocks)

wave_index = 0

def iterate_waves():
    global wave_index
    val = waves[wave_index]
    wave_index = (wave_index +1 )% len(waves)

    return val


def conflict(stone:list):
    for x,y in stone:
        if (x,y) in rocks or x<0 or x>=7:
            return True

    return False

def stone_move(stone_func):

    x,y = 2, get_max_y() + 4
    stone = stone_func(x,y)
    while True:
        wave = iterate_waves()
        # if wave:
        #     print("right")
        # else: print('left')
        new_x = x+1 if wave else x-1

        new_stone = stone_func(new_x,y)
        if not conflict(new_stone):
            x = new_x
            stone = new_stone

        new_y = y-1
        new_stone = stone_func(x,new_y)

        if not conflict(new_stone):
            y = new_y
            stone = new_stone

        else: # place stone
            for cords in stone:
                rocks[cords] = '#'
            return


def print_rocks():
    for y in range(get_max_y(),-1,-1):

        string = "|" + "".join([rocks[(x,y)] if (x,y) in rocks else '.' for x in range(7)]) + '|'

        print(string)
    
    print("\n\n")

print_rocks()
    

for i in range(2022):
    stone_move(stones[i%len(stones)])
    # print("Rock:",i+1)
    # print_rocks()

print("Part 1:", get_max_y())        


    