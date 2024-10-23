import aocd 
import timeit

data = aocd.get_data(year=2022,day=6)


s = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
s1 = "nppdvjthqldpwncqszvftbrmjlhg"
s2 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def print_first(s):

    for i in range(3,len(s)):
        if len(set(s[i-3:i+1]))==4:
            return i+1



def print_hash(s,k):

    l = {}

    for i in range(len(s)):

        c = s[i]
        if c in l:
            l[c]+=1
        else:
            l[c]=1

        if i >= k:

            l[s[i-k]] -=1
            if l[s[i-k]]==0:
                del l[s[i-k]]

            if len(l)==k:
                return i+1


print_hash(s,4)

print_first(s)
print_first(s1)
print_hash(s1,4)

print_first(s2)
print_hash(s2,4)

print_first(data)
print_hash(data,4)


def print_first2(s):

    for i in range(13,len(s)):

        if len(set(s[i-13:i+1]))==14:
            return i+1
        
print_first2(data)

k = lambda : print_first2(data)
j = lambda :print_hash(data,14)


a = timeit.timeit(k,number = 1000)
b = timeit.timeit(j,number = 1000)
print(a)
print(b)
