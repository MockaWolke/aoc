lines = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""".splitlines()

lines = open('18.txt').read().splitlines()
free = set()
encompassed = set()
cubes = set()
yzs = {}
xzs = {}
xys = {}


for l in lines:
    val = eval('('+l+')')
    
    xz = val[:1] + val[2:]
    if xz in xzs:
        xzs[xz].add(val[1])
    else:
        xzs[xz] = {val[1]}
    

    yz = val[1:]
    if yz in yzs:
        yzs[yz].add(val[0])
    else:
        yzs[yz] = {val[0]}

    xy = val[:2]
    if xy in xys:
        xys[xy].add(val[2])
    else:
        xys[xy] = {val[2] }


    cubes.add(val)


def there_is_encomppasing_elements_in_set(s:dict,key:tuple,val):

    if key not in s:
        return True

    smaller = False
    bigger = False
    for i in s[key]:
        if i<val:
            smaller = True
        if i > val:
            bigger = True
        
        if bigger and smaller:
            return False

    return True

    
def get_neighbors(cube:tuple):

    neighbors = []

    for x in [cube[0]-1,cube[0]+1]:
        neighbors.append( (x,cube[1],cube[2]) )

    for y in [cube[1]-1,cube[1]+1]:
        neighbors.append( (cube[0],y,cube[2]) )

    for z in [cube[2]-1,cube[2]+1]:
        neighbors.append( (cube[0],cube[1],z) )

    return neighbors
    

def check_free(cube,in_progress_set:set):
    """recursion"""

    if cube in in_progress_set or cube in cubes:
        return False

    in_progress_set.add(cube)

    if cube in free:
        return True

    if there_is_encomppasing_elements_in_set(xys,cube[:2],cube[2]):
        return True

    if there_is_encomppasing_elements_in_set(xzs,cube[:1] + cube[2:],cube[1]):
            return True

    if there_is_encomppasing_elements_in_set(yzs,cube[1:],cube[0]):
            return True

    for n in get_neighbors(cube):

        if n in in_progress_set or cube in cubes:
            continue

        if check_free(n,in_progress_set):
            return True

    return False





surface_area = 0

def cube_check(cube):
    global surface_area,free,cubes,encompassed

    
    for neighbors in get_neighbors(cube):  

        if neighbors in cubes or neighbors in encompassed:
            continue

        if neighbors in free:
            surface_area += 1

        else: 
            in_progress_set = set()
            if check_free(neighbors,in_progress_set):
                free = free.union(in_progress_set)
                surface_area += 1
            else:
                encompassed = encompassed.union(in_progress_set)

for cube in cubes:
    cube_check(cube)

print(surface_area)