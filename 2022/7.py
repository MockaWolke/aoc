import aocd  
import re  
data = aocd.get_data(year=2022,day=7).splitlines()


# data = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k""".splitlines()

below_10000 =[]
sizes = []


class Directory:

    def __init__(self,name:str,parent) -> None:
        assert isinstance(name,str)
        self.name = name
        self.parent = parent
        self.sub = {}

    def get_size(self):

        s = 0

        for v in self.sub:
            k = self.sub[v]

            if isinstance(k,int):
                s+=k

            else: 
                s+=k.get_size()

        if s <= 100000:
            below_10000.append(s)

        self.size = s
        sizes.append(s)
        return s


home_dir = Directory("/",None)

current_dir = home_dir


ls_mode = False

for line in data:

    if "$ cd " in line:
        ls_mode = False


    if line=="$ cd ..":
        current_dir = current_dir.parent
    elif line=="$ cd /":
        current_dir = home_dir

    elif line[:5] == "$ cd ": 

        current_dir = current_dir.sub[ line[5:]]

    elif line=="$ ls":
        ls_mode = True

    else:
        a,b = line.split()

        v = Directory(b,current_dir) if a=="dir" else int(a)
        current_dir.sub[b] = v

home_dir_size = home_dir.get_size()

print("Home dir size",home_dir_size)

# print("part 1: ",below_10000)
print("part 1: ",sum(below_10000))

# print(home_dir_size,70000000 - home_dir_size)

needed = 30000000- (70000000 - home_dir_size)
print("Space needed",needed)

for v in sorted(sizes):

    if v>needed:
        print("part 2:",v)
        break
