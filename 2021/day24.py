import aocd
import sys


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))

s = aocd.get_data(day=24,year=2021).split("inp w\n")
s = [c.splitlines() for c in s[1:]]

def calculate_part(k,n,z):
    c={"x":0,"y":0,"z":z,"w":n}
    for inss in s[k]:
        ins = inss.split()
      #  print(ins)
        com = ins[0]
        if com=="inp":
            c[ins[1]]=n
            i+=1
        else:
            if ins[2].lstrip("-").isnumeric():
                v2=int(ins[2])
            else:
                v2=c[ins[2]]

            if com=="add":
                c[ins[1]]+=v2
            elif com=="mul":
                c[ins[1]]*=v2
            elif com=="div":
                assert v2!=0, "div by 0"
                c[ins[1]]=c[ins[1]]//v2
            elif com=="mod":
                assert c[ins[1]]>=0 and v2>0, "modulo error"
                c[ins[1]]=c[ins[1]]%v2
            elif com=="eql":
                c[ins[1]]=c[ins[1]]==v2
      #  print(c)
    return c

def simulate_function(s):
    s = [c.split() for c in s]
    ins = []
    ins.append("z = za")
    if s[3][2]!="1":
        assert s[3][2]=="26"
        ins.append("z = z//26")
    if int(s[4][2])>9:
        ins.append("x=1")
        ins.append("y=26")
        ins.append("z=z*26")
    else:
        ins.append(f"x = 1- (za%26+{s[4][2]}==w)")
        ins.append("z = z * (25*x+1)")
    ins.append(f"z =z+(w+{s[-3][2]})*x")
    return ins


import os 
def write_script():
    f= open("function.txt","w+")
    f.write("# Your functions \n")
    f.close()
    for i in range(1,15):
        b=simulate_function(s[i-1])
        f = open("function.txt","a")
        f.write(f"def function_{i}(w,za):\n    "+"\n    ".join(b)+"\n    return z \n\n")
        f.close()
    os.rename("function.txt","function.py")


write_script()
from function import *


assert all([eval(f"function_{i+1}")(j,k)==calculate_part(i,j,k)["z"] for i in range(1,10) for j in range(1,10) for k in range(1000)])



a = set()
b = []
d = dict()
for i in range(1,10):
    v = function_1(i,0)
    d[v]=i
    a.add(v)
b.append(d)


import time

def solve(a):
    q=a
    global b
    t = time.time()
    for k in range(2,15):
        func = eval(f"function_{k}")
        a= set()
        d = dict()
        for j in q:
            for i in range(1,10):
                v = func(i,j)
                if v in d:
                    d[v]+=(i,j)
                else:
                    d[v]=(i,j)
                a.add(v)
        q=a
        b.append(d)
        progress(k,14,"creating all solutions")
        t = time.time()
solve(a)
b.reverse()


l = b[0][0]
sol =[]
def recu(l,level=14,val=""):
    if level!=1:
            l = list(l)
            zahlen,jts = l[::2],l[1::2]
            for i,j in enumerate(jts):
                recu(b[15-level][j],level-1,str(zahlen[i])+val)
    else:
        sol.append(int(str(l)+val))
recu(l)
    


print("\nSolutions are: ",max(sol),min(sol))

