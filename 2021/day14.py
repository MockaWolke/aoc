import numpy as np
import aocd



s = aocd.get_data(day=14,year=2021).splitlines()


start = s[0]
rest = s[2:]

transition, counts = {b[:2]:b[-1] for b in rest},{b[:2]:0 for b in rest}
for i in range(len(start)-1):
    counts[start[i:i+2]]+=1
letter_counts = {b:0 for b in {c for e in rest for c in e if c.isalpha()}}
for c in start:
    letter_counts[c]+=1



def tick():
    global transition
    global counts
    global letter_counts
    new_counts = counts.copy()
    for el in counts:
        v = counts[el]
        if v>0:
            q=transition[el]
            letter_counts[q]+=v
            a,b = el
            new_counts[a+q]+=v
            new_counts[q+b]+=v
            new_counts[el]-=v
    return new_counts
for i in range(40):
    counts = tick()
    if i==9:
        print(max(letter_counts.values())-min(letter_counts.values()))
print(max(letter_counts.values())-min(letter_counts.values()))

