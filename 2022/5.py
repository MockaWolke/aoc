import aocd  
import re  
data = aocd.get_data(year=2022,day=5).splitlines()


# data = """    [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2""".splitlines()

instructions_start = data.index("")

stacks_inputs = [list(l[1::4]).copy() for l in  data[:instructions_start-1]]

# # create Stacks

stacks = [list() for i in range(len(stacks_inputs[0]))]


for inputs in reversed(stacks_inputs):
    for i,s in zip(inputs,stacks):

        if i!=" ":
            s.append(i)

# print(stacks)

instructions = [tuple(map(int,re.findall(r"\d+",c)))  for c in data[instructions_start+1:]]

# print(instructions)

# part 1

# for times, source, target in  instructions:

#     for _ in range(times):

#         stacks[target-1].append(stacks[source-1].pop())


# part 2

for times, source, target in  instructions:

    crates = stacks[source-1][-times:]
    stacks[source-1] = stacks[source-1][:-times]

    stacks[target-1].extend(crates)


res = "".join(i[-1] for i in stacks)
print(res)
