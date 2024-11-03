from aoc import get_aoc_input
from collections import deque

data = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""
data = get_aoc_input(day=20, year=2023)


class Module:
    cases = ["%", "&", "broadcaster"]

    def __init__(self, line: str) -> None:
        if not line.startswith("broadcaster"):
            self.typ = line[0]
            line = line[1:]
        else:
            self.typ = "broadcaster"

        self.name, des = line.split(" -> ")
        self.destinations: list[str] = [i.strip() for i in des.split(", ")]
        self.name = self.name.strip()

        assert self.typ in self.cases

        if self.typ == "%":
            self.state = False
        elif self.typ == "&":
            self.state = {}

    def handle_pulse(self, pulse: bool, source: str) -> list[tuple[str, bool, str]]:
        if self.typ == "broadcaster":
            return [(i, pulse, self.name) for i in self.destinations]

        elif self.typ == "%":
            if pulse:
                return []

            self.state = not self.state
            return [(i, self.state, self.name) for i in self.destinations]

        else:
            self.state[source] = pulse
            val = not all(self.state.values())
            return [(i, val, self.name) for i in self.destinations]

def get_modules():
    modules = {}
    for line in data.splitlines():
        mod = Module(line)
        modules[mod.name] = mod

    # init conjunctions
    for key, mod in modules.items():
        for n in mod.destinations:
            if n in modules and modules[n].typ == "&":
                modules[n].state[key] = False
    return modules

def press_button():
    low = 0
    high = 0
    
    pulses = deque([("broadcaster", False, None)])
    while pulses:
        dest, val, source = pulses.popleft()
        if val:
            high += 1
        else:
            low += 1
        
        if dest not in modules:
            continue
        
        new_pulses = modules[dest].handle_pulse(val, source)
        # for dest, pul, source in new_pulses:
        #     print(f"{source} -{'high' if pul else 'low'}-> {dest}")
        
        pulses.extend(new_pulses)
        
    
    return low, high


modules = get_modules()
vals = [press_button() for _ in range(1000)]
lows, high = map(sum, zip(*vals))

print(lows, high, lows * high)



def p2():
    print("l")
    rx_low = False
    
    pulses = deque([("broadcaster", False, None)])
    while pulses:
        dest, val, source = pulses.popleft()
        
        if dest == "rx":
            print(val)
        if dest == "rx" and val == False:
            rx_low = True
        
        if dest not in modules:
            continue
        
        new_pulses = modules[dest].handle_pulse(val, source)
        
        pulses.extend(new_pulses)
        
    
    return rx_low

modules = get_modules()
i = 1
while not p2():
    i +=1
print(i)