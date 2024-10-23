import numpy as np
import aocd
import re

data = aocd.get_data(day=21,year=2021).splitlines()
game = {int(a):[int(b),0] for a,b in map(lambda x: re.findall(r'\d+',x),data)}

class Deterministic_Dye():
    def __init__(self):
        self.i=1
        self.times=0
        
    def __call__(self):
        self.times+=1
        v = self.i
        self.i+=1
        if self.i==101:
            self.i=1
        return v

Dye = Deterministic_Dye()

def tick():
    for player in game:
        game[player][0]+=np.sum([Dye() for i in range(3)])
        v = game[player][0]%10
        game[player][0] = v if v!=0 else 10
        game[player][1]+=game[player][0]
        if game[player][1]>=1000:
            return False
    return True

while tick():
    None
if game[1][1]>=1000:
    print(game[2][1]*Dye.times)
else:
    print(game[1][1]*Dye.times)

values, frequency=np.unique([a+b+c+0 for a in range(1,4) for b in range(1,4) for c in range(1,4)],return_counts=1)

start_pos = list(map(lambda x: int(re.findall(r'\d+',x)[1]),data))
start = {(start_pos[0],0,start_pos[1],0):1}

def player1(old):
    global wins_player1
    dic = {}
    for c in old:
        for i,pos_val in enumerate(values):        
            val = c[0]+pos_val
            if val>10:
                val-=10
            key =(val,c[1]+val,c[2],c[3])
            if key[1]>20:
                wins_player1+=frequency[i]*old[c]
            elif key in dic:
                dic[key]+=frequency[i]*old[c]
            else:
                dic[key]=frequency[i]*old[c]
    return dic
def player2(old):
    global wins_player2
    dic = {}
    for c in old:
        for i,pos_val in enumerate(values):        
            val = c[2]+pos_val
            if val>10:
                val-=10
            key =(c[0],c[1],val,val+c[3])
            if key[3]>20:
                wins_player2+=frequency[i]*old[c]
            elif key in dic:
                dic[key]+=frequency[i]*old[c]
            else:
                dic[key]=frequency[i]*old[c]
    return dic
x = start
wins_player1 = 0
wins_player2 = 0
while len(x):
    x = player2(player1(x))
print(wins_player1) if wins_player1> wins_player2 else print(wins_player2)