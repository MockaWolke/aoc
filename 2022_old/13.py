from aocd import get_data
# get_data(day=13,year=2022)

lines = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".split("\n\n")

lines = open("13.txt").read().split("\n\n")

pairs = []

for l in lines:
    x = l.splitlines()
    pairs.append((eval(x[0]),eval(x[1])))

index_sum = 0

def save_cast_to_list(l):
    if isinstance(l,int):
        return [l]
    elif isinstance(l,list):
        return l
    else:
        print("error")

def eval_list(left,right):

    i = 0
    while True:

        if i < len(left) and i< len(right):
            
            a,b = left[i],right[i]
            if isinstance(a,int) and  isinstance(b,int):
            
                if a<b:
                    return True
                elif a>b: 
                    return False

            else:
                
                a,b = save_cast_to_list(a), save_cast_to_list(b)
                
                val = eval_list(a,b)
                if val is not None:
                    return val
            
            i +=1
            



        elif i>=len(left) and i< len(right):
            return True
        elif i<len(left) and i >= len(right):
            return False
        else:
            return None

for index, (left,right) in enumerate(pairs,start = 1):

    val = eval_list(left,right)
    if val is None:
        print("wtf!")

    if val == True:
        index_sum+=index
    # print(left,right,f"val: {val} Sum: {index_sum}",sep="\n")

print("Part 1:",index_sum)

lines = "\n".join(lines)

lists = [eval(l) for l in lines.splitlines()]
lists.append([[2]])
lists.append([[6]])

for i in range(len(lists)):
    for b in range(1,len(lists)):

        val = eval_list(lists[b-1],lists[b])
        if val is None:
            print("DSdadsa")
        
        if val == False:
            lists[b-1],lists[b] = lists[b],lists[b-1] 

# for l in lists:
#     print(l)

part_2 = (lists.index([[2]]) +1 ) * (lists.index([[6]]) +1 ) 
print("Part 2:",part_2)