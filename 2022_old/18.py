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

cubes = set()
for l in lines:
    cubes.add(eval('('+l+')'))

surface_area = 0

def cube_check(cube):
    global surface_area
    for x in [cube[0]-1,cube[0]+1]:

        surface_area += (x,cube[1],cube[2]) not in cubes

    for y in [cube[1]-1,cube[1]+1]:

        surface_area += (cube[0],y,cube[2]) not in cubes

    for z in [cube[2]-1,cube[2]+1]:

        surface_area += (cube[0],cube[1],z) not in cubes

for cube in cubes:
    cube_check(cube)

print(surface_area)