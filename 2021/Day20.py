# A bit of brute force
import aocd
import numpy as np
convert = lambda a: np.array([[int(b=='#') for b in row] for row in a ],dtype=bool)
data = aocd.get_data(day=20,year=2021).splitlines()
# with open("test20.txt") as t:
#     data = t.read().splitlines()
dic = data[0]
new_val = lambda c: dic[c]=='#'
arr = convert(data[2:])
arr



dic[0]



def pad(a):
    if a[[0,1,-2,-1],:].any() or a[:,[0,1,-2,-1]].any():
        return np.pad(a,1)
    else:
        return a



arr=np.pad(arr,10)
arr.astype(int)


def tick(arr):
    new = arr.copy()
    for y in range(1,arr.shape[0]-1):
        for x in range(1,arr.shape[1]-1):
            neighborhood = [str(int(i)) for i in arr[y-1:y+2,x-1:x+2].flatten()]
            if neighborhood:
                v = "".join(neighborhood)
                v = int(v,2)
                new[y,x]=new_val(v)
    return new

arr = np.pad(arr,200)
for i in range(50):
    arr = tick(arr)
    if i in [1,49]:
        print(arr[55:-55,55:-55].sum())





