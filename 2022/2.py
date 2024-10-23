from aocd import get_data

scores = {"A":1,'B':2,'C':3,"X":1,'Y':2,'Z':3}

beats = {(1,2),(2,3),(3,1)}

data = []

inputs = get_data(year=2022,day=2).split("\n")

for l in inputs:

    data.append( (scores[l[0]],scores[l[2]]))

scores = 0

for l in data:
    scores += l[1]

    if l[0]==l[1]:
        scores +=3
    elif l in beats:
        scores +=6

print(scores)


win = lambda x: (x+1)%4 + ((x+1)==4)
loss = lambda x: (x-1)%4 + ((x-1)==0) * 3

new_scores = 0 

for l in data:

    if l[1]==1:
        new_scores += loss(l[0])
    elif l[1]==2:
        new_scores += l[0] + 3
    else:
        new_scores += win(l[0]) + 6

print(new_scores)
