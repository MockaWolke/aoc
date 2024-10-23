import numpy as np
import aocd
costs = {"(":3,"[":57,"{":1197,"<":25137}
costs2 = {"(":1,"[":2,"{":3,"<":4}



dic = {"(":")","[":"]","{":"}","<":">"}
dic_swi = {dic[a]:a for a in dic}

s = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".splitlines()
s = aocd.get_data(day=10,year=2021).splitlines()




l = []
b = 0
for r in s:
    stack = []
    i = 0
    for i,c in enumerate(r):
        if c in dic:
            stack.append(c)
        else:
            f = stack.pop()
            if dic[f] !=c:
                b+=costs[dic_swi[c]]
                break
    if i==len(r)-1 and len(stack):
        k = 0
        while stack:
            k*=5
            k+=costs2[stack.pop()]
        l.append(k)


l.sort()
print(b,l[len(l)//2])


