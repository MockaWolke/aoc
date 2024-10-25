import re
import numpy as np
lines = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""".splitlines()

lines = open('21.txt').read().splitlines()



def parse_inputs(lines):
    numbers = {}
    op_monkey = {}
    tells = {}

    for k in lines:
        l = k.split(" ")
        name = l[0][:-1]


        imp = l[1]
        if imp.isnumeric():
            numbers[name] = int(imp)

        else:
            m1,m2 = l[1],l[3]
            func = eval(f"lambda {m1},{m2} {k[k.find(':'):]}")

            op_monkey[name] = (m1,m2,func)
            for m in [m1,m2]:
                if m in tells:
                    tells[m].append(name)
                else:
                    tells[m] = [name]

    return numbers,op_monkey,tells

def forward_pass():
    global numbers, op_monkey,tells
    q = list(numbers.keys())
    been_there = set()

    while q:
        monkey = q.pop(0)

        if monkey not in tells or monkey in been_there:
            continue

        been_there.add(monkey)

        for waiter in tells[monkey]:
            m1,m2,op = op_monkey[waiter]
            if m1 in numbers and m2 in numbers:
                numbers[waiter] = op(numbers[m1],numbers[m2])
                if numbers[waiter] != int(numbers[waiter]):
                    print("FLOAT ERROR")
                numbers[waiter] = int(numbers[waiter])
                q.append(waiter)

numbers,op_monkey,tells = parse_inputs(lines)
forward_pass()
print("Part 1:",numbers['root'])


levels = {}

def build_computation_tree(current,level):
    global levels
    if level in levels:
        levels[level].append(current)
    else:
        levels[level] = [current]

    if current not in tells:
        return

    for m in tells[current]:
        build_computation_tree(m,level+1)
        
build_computation_tree('humn',0)

print(all(len(i)== 1 for i in levels.values()))

goal = set(op_monkey['root'][:2]).difference(list(levels.values())[-2])
goal = tuple(goal)[0]
print(goal,numbers[goal])

correct_number = numbers[goal]

def reverse_op(op,goal_number,support,support_left):

    new_op =lambda x,y: print("error op")
    res = op(6,3)
    if res == 9:
        return goal_number-support
        
    elif res==3 and not support_left:
        return support + goal_number
        
    elif res==3 and support_left:
        return support - goal_number
    
    elif res==18:
        
        return goal_number/support

    elif res==2 and support_left:
        return support/goal_number
    elif res==2 and not support_left:
        return support * goal_number
        

    if support_left:
        return new_op(support,goal_number)
    else:
        return new_op(goal_number,support)


comp = [i[0] for i in levels.values()]
comp = list(reversed(comp[:-1]))

human_number = 0

back_track = [correct_number]

for i,com in enumerate(comp):
    if com=='humn':
        print('humn',i,len(comp),correct_number)
        human_number = correct_number
        break


    m1,m2, op = op_monkey[com]

    if m1 in comp and m2 in comp:
        print("damn")

    if m1==comp[i+1]:
        support = numbers[m2]
        support_left = False
    elif m2==comp[i+1]:
        support = numbers[m1]
        support_left = True
    else:
        print("error",com)
    old_correct_number = correct_number
    correct_number = reverse_op(op,correct_number,support,support_left)

    check = op(support,correct_number) if support_left else op(correct_number,support)
    if not np.allclose(check,old_correct_number):
        print("damn",old_correct_number,check,support,support_left,op(6,3),correct_number)
        exit()
        break
    back_track.append(correct_number)

print("correct_number",correct_number)



lines = open('21.txt').read().splitlines()

numbers,op_monkey,tells = parse_inputs(lines)

numbers['humn'] = human_number

forward_pass()

print(numbers['root'])
print(numbers['qmfl'],numbers[goal])
# print(back_track)

# good_backtrack = {a:b for a,b in zip(comp,back_track)}
# for num,com in zip(back_track,comp):

#     m1,m2, op = op_monkey[com]

#     n1,n2 = numbers[m1],numbers[m2]

#     if m1 in good_backtrack:
#         n1 = good_backtrack[m1]
    
#     elif m2 in good_backtrack:
#         n2 = good_backtrack[m2]
#     else:
#         print("doam!")

#     if op(n1,n2)!=num:

#         print("error",num,com,m1,n1,m2,n2,op(6,3),op(n1,n2))
#         break
#     print("pass")


