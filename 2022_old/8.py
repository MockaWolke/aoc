import numpy as np

with open("5.txt","r") as f:
    lines = f.read().splitlines()

# lines = """30373
# 25512
# 65332
# 33549
# 35390
# """.splitlines()

field = np.array([[int(i) for i in l]for l in lines])

def get_min_field(field):

    # min vector down
    min_row = np.ones_like(field[0]) * -1
    rows = []
    for i in range(len(field)):

        rows.append(min_row)

        min_row = np.maximum(min_row,field[i])

    return np.stack(rows)


max_fied = np.ones_like(field) * 9



for i in range(4):

    rot = np.rot90(field,i)
    min_field = get_min_field(rot)
    back = np.rot90(min_field,-i)

    max_fied = np.minimum(max_fied,back)


mask = max_fied < field
print("p1",mask.sum())


def get_senic_score(x,y):

    current = field[x,y]
    p = 1
    for i in range(4):
        cx,cy = x,y
        
        counter = 1
        while True:
            if i==0:
                cx+=1
            elif i == 1:
                cy+=1
            elif i==2:
                cx-=1
            else:
                cy-=1

            if 0 <= cx < len(field) and 0 <= cy < len(field):
                if field[cx,cy] >= current:
                    break
                else:
                    counter += 1
            else:
                counter-=1
                break

        p*=counter
    return p


p2 = np.zeros_like(field)
for x in range(len(field)):
    for y in range(len(field)):
        p2[x,y] = get_senic_score(x,y)

print("p2",p2.max())