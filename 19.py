from aoc import get_aoc_input

data = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""
data = get_aoc_input(19,2023)


rules_raw, parts_raw = data.split("\n\n")

rules = {}

for line in rules_raw.splitlines():
    
    key = line[:line.find("{")]
    sub = line[line.find("{") + 1:-1].split(",")
    
    commands = []
    
    def process_symbol(s : str, symbol : str):
        atr,rest = s.split(symbol)
        val, goal = rest.split(":")
        val = int(val)
        
        if symbol == ">":
            return (">",atr, val, goal)
        
        return ("<",atr, val, goal)
        
    
    for s in sub:
        if ">" in s:
            commands.append(process_symbol(s, ">"))
        elif "<" in s:
            commands.append(process_symbol(s, "<"))
        else:
            commands.append(s)
        
        
    rules[key] = commands
    


parts = []
for l in parts_raw.splitlines():
    
    part = {}
    for s in l[1:-1].split(","):
        key,val = s.split("=")
        part[key] = int(val)
    
    parts.append(part)


def apply(data, cmd):
    if isinstance(cmd, str):
        return cmd
    
    if cmd[0] == ">":
        return cmd[-1] if data[cmd[1]] > cmd[2] else None

    return cmd[-1] if data[cmd[1]] < cmd[2] else None
    
def apply_rule(data, command):
    for func in command:
        v = apply(data, func)
        if v is None:
            continue
        return v
        

def asses_part(part, rule_key):
    
    v = apply_rule(part, rules[rule_key])
    if v == "A":
        return True
    if v == "R":
        return False
    return asses_part(part, v)



part1 = 0

for part in parts:
    if asses_part(part, "in"):
        part1 += sum(part.values())
    
print(part1)