from aoc import get_aoc_input

data = get_aoc_input(19,2023)


rules_raw, parts_raw = data.split("\n\n")

rules = {}

for line in rules_raw.splitlines():

    key = line[: line.find("{")]
    sub = line[line.find("{") + 1 : -1].split(",")

    commands = []

    def process_symbol(s: str, symbol: str):
        atr, rest = s.split(symbol)
        val, goal = rest.split(":")
        val = int(val)

        if symbol == ">":
            return (">", atr, val, goal)

        return ("<", atr, val, goal)

    for s in sub:
        if ">" in s:
            commands.append(process_symbol(s, ">"))
        elif "<" in s:
            commands.append(process_symbol(s, "<"))
        else:
            commands.append(s)

    rules[key] = commands


start_bound = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}

agenda = [(start_bound, "in")]

sucess = []

while agenda:
    bounds, rule_key = agenda.pop()

    if rule_key == "A":
        sucess.append(bounds.copy())
        continue

    if rule_key == "R":
        continue
    for comp, atr, val, goal in rules[rule_key][:-1]:

        if comp == ">" and bounds[atr][1] > val:
            new_bounds = bounds.copy()
            new_bounds[atr] = (max(val + 1, bounds[atr][0]), bounds[atr][1])
            agenda.append((new_bounds, goal))

            if bounds[atr][0] <= val:
                bounds[atr] = (bounds[atr][0], val)
            else:
                break

        elif comp == "<" and bounds[atr][0] < val:
            new_bounds = bounds.copy()
            new_bounds[atr] = (bounds[atr][0], min(val - 1, bounds[atr][1]))
            agenda.append((new_bounds, goal))

            if bounds[atr][1] >= val:
                bounds[atr] = (val, bounds[atr][1])
            else:
                break

    else:
        agenda.append((bounds.copy(), rules[rule_key][-1]))



val = 0

for bounds in sucess:
    prod = 1
    for a, b in bounds.values():
        prod *= b + 1 - a
    val += prod

print(val)
