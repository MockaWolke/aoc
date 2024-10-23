import aocd
outputs = [c.split(" | ")[1].split() for c in aocd.get_data(day=8,year=2021).splitlines()]
encoding = [c.split(" | ")[0].split() for c in aocd.get_data(day=8,year=2021).splitlines()]

count = 0
for i in outputs:
    for b in i:
        if len(b) in [2,4,3,7]:
            count+=1
print(count)

overlap = lambda a,b: len([c for c in a if c in b])

def decode(en):
    d = {}
    en_c = en.copy()
    for b in en:
        if len(b)==2:
            d[1]=b
        elif len(b)==3:
            d[7]=b
        elif len(b)==7:
            d[8]=b
        elif len(b)==4:
            d[4]=b
    for b in en:
        if len(b)==5 and overlap(d[7],b)==3:
            d[3]=b
        elif len(b)==5 and overlap(d[4],b)==3:
            d[5]=b
        elif len(b)==5 and overlap(d[4],b)==2:
            d[2]=b
            
    for b in en:
        if len(b)==6 and overlap(d[3],b)==5:
            d[9]=b
        elif len(b)==6 and overlap(d[1],b)==2:
            d[0]=b
        elif len(b)==6 and overlap(d[4],b)!=2:
            d[6]=b
    return {d[a]:a for a in d}



overlap = lambda a,b: len([c for c in a if c in b])

def decode(en):
    d = {}
    en_c = en.copy()
    for b in en:
        if len(b)==2:
            d[1]=b
        elif len(b)==3:
            d[7]=b
        elif len(b)==7:
            d[8]=b
        elif len(b)==4:
            d[4]=b
    for b in en:
        if len(b)==5 and overlap(d[7],b)==3:
            d[3]=b
        elif len(b)==5 and overlap(d[4],b)==3:
            d[5]=b
        elif len(b)==5 and overlap(d[4],b)==2:
            d[2]=b
            
    for b in en:
        if len(b)==6 and overlap(d[3],b)==5:
            d[9]=b
        elif len(b)==6 and overlap(d[1],b)==2:
            d[0]=b
        elif len(b)==6 and overlap(d[4],b)!=2:
            d[6]=b
    return {d[a]:a for a in d}

count = 0
for e,o in zip(encoding,outputs):
    code = decode(e)
    for i,z in enumerate(o):
        for key in code:
            if overlap(key,z)==len(z)==len(key):
                count+=10**(3-i)*code[key]
                break
print(count)