import aocd 
import re
import numpy as np

data = aocd.get_data(year=2021,day=4).splitlines()

numbers = list(map(int,re.findall(r'\d+',data[0])))

fields = "\n".join(data[2:]).split("\n\n")

class Bingo:
    def __init__(self,field) -> None:
        
        numbers = list(map(int,re.findall(r'\d+',field)))
        self.field = np.array(numbers).reshape(5,5)
        self.hits = np.zeros((5,5))

    def done(self):
        return np.any(self.hits.sum(axis=1) == 5) or np.any(self.hits.sum(axis=0) == 5)

    def hit(self,number):

        for x,y in np.argwhere(self.field == number):
            self.hits[x,y] = 1

        if self.done():

            vals = np.sum([self.field[x,y] for x,y in np.argwhere(self.hits == 0)])
            return vals*number


fields = [Bingo(f) for f in fields]

first = 0
last = 0

while numbers:
    n = numbers.pop(0)
    remove = []
    for b in fields:

        val = b.hit(n)
        if val:
            remove.append(b)
            if first == 0:
                first = val
            last = val

    for f in remove:
        fields.remove(f)

print(first,last)    