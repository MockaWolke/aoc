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

rocks = {0:{i for i in range(7)}}

max_y = 0
min_y = 0

wave_index = 0

def iterate_waves():
    global wave_index
    val = waves[wave_index]
    wave_index = (wave_index +1 )% len(waves)

    return val


def conflict(stone:list):
    for x,y in stone:

        if x<0 or x>=7:
            return True
        if y in rocks and x in rocks[y]:
            return True
    return False

def stone_move(stone_func):
    global max_y
    x,y = 2, max_y + 4
    stone = stone_func(x,y)
    while True:
        wave = iterate_waves()

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
            for x,y in stone:
                max_y = max(y,max_y)
                if y in rocks:
                    rocks[y].add(x)
                else:
                    rocks[y] = set((x,))
            return



p2 = 10000
    
def og_val():
    global rocks,max_y,wave_index,p2
    wave_index = 0
    rocks = {0:{i for i in range(7)}}
    max_y = 0

    for i in tqdm.tqdm(range(p2)):
        stone_move(stones[i%len(stones)])
    print("Last Wave index :",wave_index)

    return max_y


def find_cycle():
    
    global rocks, max_y,wave_index,p2
    wave_index = 0
    rocks = {0:{i for i in range(7)}}
    max_y = 0
    cycle = {}

    for i in tqdm.tqdm(range(p2)):
        stone_move(stones[i%len(stones)])

        if len(rocks[max_y])==7:

            key = (wave_index ,i%len(stones))
            if key in cycle:
                print("Last Wave index :",wave_index)
                return i,max_y,cycle[key],key
            else:
                cycle[key] = (i,max_y)



def part_2():
    global rocks, max_y,wave_index,p2

    new_step, high, (beginn, old_high),(cycle_wave,cycle_stones) = find_cycle()
    step_size = new_step - beginn
    build_to = high - old_high

    amount_of_cycles = (p2 - beginn) // step_size
    wave_index = cycle_wave

    new_start = old_high + amount_of_cycles * build_to



    rocks = {new_start:{i for i in range(7)}}
    max_y = new_start


    for i in range((beginn + step_size * amount_of_cycles)+1,p2):
        stone_move(stones[i%len(stones)])

    return max_y

test_vals = [10000,22323,23323,12321,10004]
p2 = 0
for val in test_vals:
    p2 = val

    assert og_val() == part_2()

p2 = 1000000000000

print("Part 2:", part_2()  )        



    