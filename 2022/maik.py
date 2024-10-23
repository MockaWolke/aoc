import aocd

data = aocd.get_data(year=2022,day=1).split("\n\n")

elves = [sum(map(int,line.split("\n"))) for line in data]

print(max(elves))

s = 0

for i in range(3):

    v = max(elves)
    s+= max(elves)
    elves.remove(v)

print(s)