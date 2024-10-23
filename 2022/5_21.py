import aocd 
import re

data = aocd.get_data(year=2021,day=5).splitlines()


# data = """0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2""".splitlines()
print(data)

m = {}

def hit(x,y):

    m[(x,y)] = m[(x,y)]+1 if (x,y) in m else 1
    
for line in data:

    vals = re.findall(r"\d+",line)

    x1,y1,x2,y2 = map(int,vals)

    if y1==y2:
        for x in range(min(x1,x2),max(x1,x2)+1):
            hit(x,y1)


    if x1==x2:
        for y in range(min(y1,y2),max(y1,y2)+1):
            hit(x1,y)

danger = sum(i >= 2 for i in m.values())

print(danger)



m = {}

def hit(x,y):

    m[(x,y)] = m[(x,y)]+1 if (x,y) in m else 1
    
for line in data:

    vals = re.findall(r"\d+",line)
    x1,y1,x2,y2 = map(int,vals)
    
    
    if y1==y2:
        for x in range(min(x1,x2),max(x1,x2)+1):
            hit(x,y1)


    elif x1==x2:
        for y in range(min(y1,y2),max(y1,y2)+1):
            hit(x1,y)

    else:
        x_range =  range(x1,x2) if x1< x2 else range(x1,x2-1,-1)
        
        y_range = range(y1,y2+1) if y2>y1 else range(y1,y2-1,-1) 

        for x,y in zip(x_range,y_range):
            hit(x,y)
danger = sum(i >= 2 for i in m.values())

print(danger)