import aocd
import numpy as np
s = aocd.get_data(day=16,year=2021)
tbin = lambda s : "".join([f'{int(c,16):04b}'for c in s])
s = tbin(s)



q = 0
def parse(s):
    global q
    v_num = int(s[:3],2)
    q+=v_num
    t_id = int(s[3:6],2)
    if t_id==4:
        i = 6
        c = ""
        o = True
        while o:
            o = s[i]=="1"
            c+= s[i+1:i+5]
            i+=5
        return int(c,2),s[i:]
    else:
        vals = []
        if s[6]=="0":
            l = int(s[7:22],2)
            p,n = s[22:22+l],s[22+l:]
            while len(p):
                v,p = parse(p)
                vals.append(v)
        else:
            t = int(s[7:18],2)
            p = s[18:]
            for ü in range(t):
                v,p = parse(p)
                vals.append(v)
            n = p
        if len(vals)==0:
            print("wtf")
        if t_id==0:
            return np.sum(vals),n
        if t_id==1:
            return np.prod(vals),n
        if t_id ==2:
            return np.min(vals),n
        if t_id ==3:
            return np.max(vals),n
        if t_id ==5:
            return vals[0]>vals[1],n
        if t_id ==6:
            return vals[1]>vals[0],n
        if t_id ==7:
            return int(vals[1]==vals[0]),n



print(f"Part 2: {parse(s)[0]} Part 1: {q}")


