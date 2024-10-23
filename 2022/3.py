import aocd 
data = aocd.get_data(year=2022,day=3).splitlines()



def get_prio(char):

    minus = ord('a') -1 if char.islower() else ord('A')-27
    return ord(char)-minus

total_prio = 0

for line in data:

    l = len(line)//2
    first,second = line[:l],line[l:]

    inter = set(first).intersection(second)
    vals = list(map(get_prio,inter))
    total_prio += sum(vals)

print(total_prio)

group_prios = 0

for l1,l2,l3 in zip(data[::3],data[1::3],data[2::3]):

    inter = set(l1).intersection(l2).intersection(l3)
    vals = list(map(get_prio,inter))
    group_prios += sum(vals)

print(group_prios)