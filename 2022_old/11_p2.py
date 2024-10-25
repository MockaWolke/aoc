from aocd import get_data
import re 
from math import prod

lines = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".split("\n\n")

# print(lines)
# lines = get_data(day=11,year=2022).split("\n\n")

class Monkey:

    def __init__(self, defining_string:str) -> None:
        
        defining_string = defining_string.splitlines() 

        # print(defining_string)

        self.number = int(re.findall(r"\d+",defining_string[0])[0])

        self.items = list(map(int,re.findall(r"\d+",defining_string[1])))

        # print(self.items,self.number)

        self.operation = eval("lambda old: " + defining_string[2][defining_string[2].find("=")+1:])
        self.test_val = int(re.findall(r"\d+",defining_string[3])[0])
        self.test = lambda x: (x%self.test_val)==0
        
        self.if_true = int(re.findall(r"\d+",defining_string[4])[0])
        self.if_false = int(re.findall(r"\d+",defining_string[5])[0])

        # print(self.operation,self.operation(1),self.test_val,self.if_true,self.if_false)

        self.inspect_count = 0

    def process(self,val):
        global global_dif
        self.inspect_count +=1

        val = self.operation(val)
        val = val%global_dif

        if self.test(val):

            monkeys[self.if_true].items.append(val)
        else:
            monkeys[self.if_false].items.append(val)

    def call(self):
        while self.items:

            self.process(self.items.pop(0))

    def __str__(self) -> str:
        
        return f"""Monkey {self.number}:
  Starting items: {self.items}
  Operation: {self.operation}, {self.operation(1)}
  Test: divisible by {self.test_val}
    If true: throw to monkey {self.if_true}
    If false: throw to monkey {self.if_false}
"""

monkeys = []

for i,l in enumerate(lines):

    m = Monkey(l)
    monkeys.append(m) 

global_dif = prod([m.test_val for m in monkeys])
print("Global Dif:",global_dif)

def round(n):
    for m in monkeys:
        m.call()

    start = f"After round {n+1}, the monkeys are holding items with these worry levels:\n"
    for i,m in enumerate(monkeys):
        start = start + f"Monkey {i}: {m.items}\n".replace("[","").replace("]","")
    return start
    
for r in range(10000):

    round(r)
    if (r+1)== 20 or (r+1)%1000==0:
        counts = [m.inspect_count for m in monkeys]
        print(r,counts)


counts = [m.inspect_count for m in monkeys]
one = max(counts)
print(counts)
counts.remove(one)
print("Part 2: ",one*max(counts))
