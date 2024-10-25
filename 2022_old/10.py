from aocd import get_data
import matplotlib

lines = get_data(day=10,year=2022).splitlines()
lines = open('10.txt').read().splitlines()

cycle = 1
x = 1

running_sum = 0

result = ""


def process_cycle():
    global cycle,x, running_sum,result
    if (cycle-20)%40==0 and cycle <= 220:
        print(cycle,x,x*cycle)
        running_sum += x*cycle

    pos = (cycle -1)%40
    if (x-1)<= pos <= (x+1):
        result = result+ '#'
    else:
        result = result+ '.'


for l in  lines:

    if l[:3]=="noo":

        cycle +=1
        process_cycle()
        continue
    
    cycle +=1
    process_cycle()
    cycle +=1
    val = int(l.split(" ")[1])
    x+=val
    process_cycle()

print("Part 1:",running_sum)

img = []
for i in range(len(result)//40):
    v = result[i*40:(i+1)*40]
    img.append([i=='#' for i in v])
    print(v)

import numpy as np
import matplotlib.pyplot as plt
plt.imshow(np.stack(img))
plt.axis("off")
plt.show()
