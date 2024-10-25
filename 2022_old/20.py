import tqdm
numbers = [1,2,-3,3,-2,0,4]

numbers = [int(c) for c in open("20.txt").read().splitlines()]


class N():
    def __init__(self,v,index) -> None:
        
        self.val = v
        self.before= None
        self.nex = None
        self.id = index


def set_up_number_list(numbers):
    number_list = {i:N(v,i) for i,v in enumerate(numbers)}

    for i,n in enumerate(numbers):
        number_list[i].before = number_list[(i-1)%len(numbers)]
        number_list[i].nex = number_list[(i+1)%len(numbers)]
    return number_list


def move(index,n,number_list):

    if abs(n)%(len(numbers)-1)==0:
        if n!= 0: print(n)
        return

    i = number_list[index]
    og_before= i.before
    og_nex= i.nex
    curent = i

    if n>0:
        
        for _ in range(n%(len(numbers)-1)):
            curent = curent.nex

        i.nex = curent.nex
        i.nex.before= i
        curent.nex = i
        i.before = curent

    elif n< 0:

        for _ in range((-n)%(len(numbers)-1)):
            curent = curent.before
        i.before = curent.before
        curent.before = i
        i.nex = curent
        i.before.nex = i
    
    og_before.nex = og_nex
    og_nex.before = og_before


def get_numbers_from(n):
    index = numbers.index(n)
    s = [n]
    old_index = number_list[index].id

    current = number_list[index].nex
    while current.id != old_index:
        s.append(current.val)
        current = current.nex
    return s

def mix(numbers,number_list):
    for i,n in enumerate(numbers):
        move(i,n,number_list)

def get_res():
    from_0 = get_numbers_from(0)

    val = 0

    for i in range(1,4):
        v = from_0[(1000*i)%len(from_0)]
        print(v)
        val +=v

    return val

number_list = set_up_number_list(numbers)

mix(numbers,number_list)

part_1 = get_res()

print("part 1:",part_1)

decryption_key =811589153
numbers = [i*decryption_key for i in numbers]

number_list = set_up_number_list(numbers)
for i in range(10):
    mix(numbers,number_list)

part_2 = get_res()

print('Part 2:',part_2)
