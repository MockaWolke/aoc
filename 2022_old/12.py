import heapq
import tqdm

lines = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines()

lines = open("12.txt").read().splitlines()

Y = len(lines)
X = len(lines[0])
print(Y,X)

m = {(y,x):ord(c)-ord('a') for y,l in enumerate(lines) for x,c in enumerate(l)}

start = [k for k in m if m[k]==(ord('S')-ord('a'))][0]
goal = [k for k in m if m[k]==(ord('E')-ord('a'))][0]

m[start] = 0
m[goal] = ord('z') - ord('a')

print(start,goal)


def get_neighbors(cords):
    x,y = cords
    current = m[cords]

    neighors = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    res = []
    for n in neighors:
        
        if n in m and (m[n] <= current+1) :

            res.append(n)
    return res



def calculate_len(start):

    q = [(0,start)]
    been_there = set()
    heapq.heapify(q)

    while q:
        steps,current = heapq.heappop(q)
        if current in been_there:
            continue
        been_there.add(current)


        if goal == current:
            return steps

        for n in get_neighbors(current):
            if  n not in been_there:
                heapq.heappush(q,(steps+1,n))

    return None

print("Part 1:",calculate_len(start))

lowest = [a for a in m if m[a]==0]

res = []

for start in tqdm.tqdm(lowest):
    val = calculate_len(start)
    if val is not None:
        res.append(val)

print("Part 2:", min(res))