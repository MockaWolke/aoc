from aoc import get_aoc_input

data = get_aoc_input(15, 2023)

def holiday_hash(s : str):
    val = 0
    
    for c in s:
        val += ord(c)
        val *=  17
        val %= 256
    return val


val = sum(holiday_hash(s) for s in data.replace("\n","").split(","))

print(val)


boxes = [dict() for _ in range(256)]


for s in data.replace("\n","").split(","):
    op = "=" if "=" in s else "-"
    key,val = s.split(op)
    
    box = boxes[holiday_hash(key)]

    if op == "-":
        if key not in box:
            continue
    
        del box[key]

    else:
        box[key] = val
        

part2 = 0

for i,box in enumerate(boxes, start=1):
    for j, (_,v) in enumerate(box.items(), start=1):
        part2 += i*j*int(v)
print(part2)