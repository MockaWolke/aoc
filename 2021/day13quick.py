import aocd
import numpy as np
import matplotlib.pyplot as plt
field, folds =  aocd.get_data(day=13,year=2021).split("\n\n")
field = np.array([[int(b) for b in c.split(",")]  for  c in field.splitlines()])
board = np.zeros((field[:,1].max()+1,field[:,0].max()+1))

for x,y in field:
    board[y,x]=1
folds = [b[11:].split("=") for b in folds.splitlines()]

def fold(command,ar):
    axis, l = command
    l = int(l)
    if axis =='x':
        return np.logical_or(ar[:,:l],ar[:,l+1:][:,::-1])
    else:
        return np.logical_or(ar[:l],ar[l+1:][::-1])

        
for i,f in enumerate(folds):
    board = fold(f,board)
    if i ==0:
        print("Part 1", board.sum())

plt.imshow(board)
plt.show()