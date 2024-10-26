from aoc import get_aoc_input
import re
from tqdm import tqdm

data = get_aoc_input(day=12, year=2023)

def get_next_pos(s: str, n: tuple[int], i=0):

    while i < len(s) and s[i] != "?":
        i += 1
    if i == len(s):
        return
    
    surrounding = 0
    
    x = i+-1
    while x > -1 and s[x] == "#":
        surrounding += 1
        x -= 1
    l_border = x +1
    
    
    x = i+1
    while x < len(s) and s[x] == "#":
        surrounding += 1
        x += 1

    q_following = x < len(s) and s[x] == "?"
    
    if l_border > 0:
        splits = re.split(r'[.?]', s[:l_border])
        until = tuple(len(j) for j in splits if len(j))
        
        
    else:
        until = tuple()
    
    if until != n[:len(until)]:
        return None
    elif until == n:
        return "yes"
    
    m = n[len(until)]
    
    if m > surrounding:
        return i, surrounding, q_following, n, m, s
    
    # in this case we are jumping to next
    s = insert_to_string(s, i, '.')

    return get_next_pos(s, n, i + 1)


def insert_to_string(s, i, char):
    return s[:i] + char + s[i + 1 :]

def count_pos(s, n, done : dict[str,int], i=0):
    input_s = s
    if s in done:
        return done[s]
    
    
    old_s = s
    while ".." in s[:i]:
        s = s[:i].replace("..",".") + s[i:]
    if old_s != s:
        i = max(i - (len(old_s) - len(s)), 0)
    if len(old_s) < len(s):
        print("wtf")
        return 0
    
    if len(s.replace(".","")) < sum(n):
        done[s] = 0
        return 0
    
    splits = re.split(r'[.?]', s)
    until = tuple(len(j) for j in splits if len(j))
    
    if until == n:
        done[s] = 1
        return 1

    val = get_next_pos(s, n, i)
    
    if val is None or val == "yes":
        done[s] = 0
        return 0
    
    next_pos, sorrounding, q_following, n, m, s = val
    dot_case = count_pos(insert_to_string(s, next_pos, "."), n, done, next_pos + 1)
    
    
    # if the wanted digit is more than we can offer and there is no ? at the end
    if m > sorrounding +1  and q_following == False:
        val =  dot_case
    else: 
        hash_case = count_pos(insert_to_string(s, next_pos, "#"), n, done, next_pos + 1)
        val = dot_case + hash_case
    
    done[input_s] = val
    done[s] = val
    return val


p1,p2 = 0,0
for line in tqdm(data.splitlines()):
    s, n = line.split()
    n = tuple(map(int, n.split(",")))
    done = {}
    p1 += count_pos(s, n, done)

    s = "?".join(s for _ in range(5))
    n = 5 * n
    done = {}
    p2 += count_pos(s, n, done)    

print(p1, p2)