import aocd 
import re

data = aocd.get_data(year=2022,day=4).splitlines()

total_sum = 0
overlap_sum = 0


for line in data:

    vals = re.findall(r"\d+",line)
    a,b,c,d = map(int,vals)

    if (a<=c and b >= d) or (c<=a and d >= b):
        total_sum+=1

    if (c<=b and a<=c) or (c<= a and d>=a):
        overlap_sum += 1

print(total_sum,overlap_sum)