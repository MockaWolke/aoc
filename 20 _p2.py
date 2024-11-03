from aoc import get_aoc_input
from collections import deque
from math import lcm

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
        self.sources : list[str] = []

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

    def __hash__(self) -> int:
        
        if self.typ == "broadcaster":
            return 0

        elif self.typ == "%":

            return self.state

        else:
            return hash(tuple(self.state.values()))
        

def get_modules():
    modules = {}
    for line in data.splitlines():
        mod = Module(line)
        modules[mod.name] = mod

    # init conjunctions
    for key, mod in modules.items():
        for n in mod.destinations:
            if n in modules:
                if modules[n].typ == "&":
                    modules[n].state[key] = False
                modules[n].sources.append(key)
                
    return modules




def find_subnet(node):
    h = set()
    agenda = [node]
    
    
    while agenda:
        n = agenda.pop()
        h.add(n)
        for i in modules[n].sources:
            if i in h or i == "broadcaster":
                continue
            
            agenda.append(i)
    return h
        



def round_sub_net(node : str, net : set[str]):
    high = False
    
    pulses = deque([("broadcaster", False, None)])
    while pulses:
        dest, val, source = pulses.popleft()
        
        if source == node and val:
            high = True
        
        if dest not in net and dest != "broadcaster":
            continue
        
        new_pulses = modules[dest].handle_pulse(val, source)
        
        pulses.extend(new_pulses)
        
    
    return high


def find_cycle(node : str, net : set) -> list[int]:
    
    frozen = tuple(sorted(net))
    cycles = {}
    i = 0
    history = []
    while True:

        i += 1
        
        if round_sub_net(node, net):
            
            history.append(i)
            
            states = hash(tuple(modules[n].__hash__() for n in frozen))
            
            
            if states in cycles:
                return i, cycles[states], history
            
            cycles[states] = i






modules = get_modules()
last = [n for n,m in modules.items() if "rx" in m.destinations]
assert len(last) == 1
last = last[0]
ns = [n for n,m in modules.items() if last in m.destinations]


subnets = {n:find_subnet(n) for n in modules}


sets = {n:find_subnet(n) for n in ns}
for s in sets.values():
    
    assert all(len(i.intersection(s)) == 0 for i in sets.values() if i != s)

important = []

for relevant in ns:
    current, first, history = find_cycle(relevant, sets[relevant])
    
    assert len(history) == 2
    assert current/first == 2.0
    important.append(first)
    

print(lcm(*important))