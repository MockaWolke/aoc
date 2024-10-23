import aocd 
import re

data = aocd.get_data(year=2022,day=6)#.splitlines()


s = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
s1 = "nppdvjthqldpwncqszvftbrmjlhg"
s2 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def print_first(s):

    for i in range(3,len(s)):
        # print(i,s[i-3:i+1],set(s[i-3:i+1]))
        if len(set(s[i-3:i+1]))==4:
            print(i+1)
            break

print_first(s)
print_first(s1)
print_first(s2)
print_first(data)

def print_first2(s):

    for i in range(13,len(s)):
        # print(i)
        # print(i,s[i-3:i+1],set(s[i-3:i+1]))
        if len(set(s[i-13:i+1]))==14:
            print(i+1)
            break
        
print_first2(data)