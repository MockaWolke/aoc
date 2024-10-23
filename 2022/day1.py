from aocd import get_data

data = get_data(year=2022,day=1).split("\n\n")

elves =[sum(map(int,line.split("\n"))) for line in data]
print(max(elves))

print(sum(sorted(elves)[-3:]))
