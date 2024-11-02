from aoc import get_aoc_input
from helpers import tuple_add, tuple_mul
from collections import deque
from rectangle import Rectangle
from typing import List, Set, Optional

dir_to_diff = {
    "R": (1,0),
    "D": (0, 1),
    "L": (-1,0),
    "U": (0,-1),
}
    
def get_solution(border_lines: List[Rectangle]) -> int:
    y_start, y_end = min(r.y_start for r in border_lines), max(r.y_end for r in border_lines)
    x_start, x_end = min(r.x_start for r in border_lines), max(r.x_end for r in border_lines)
    bounding_rectangle = Rectangle(x_start, y_start, x_end, y_end)

    free_blocks = [bounding_rectangle]

    for line in border_lines:
        free_blocks = split_free_blocks(free_blocks, line)

    assert all(get_intersect(block, border_lines) is None for block in free_blocks), "Intersection found in free blocks"

    outside, inside = classify_blocks(free_blocks, border_lines, x_start, y_start, x_end, y_end)

    total_area = sum(r.area for r in inside) + sum(r.area for r in border_lines)
    return total_area

def get_intersect(rect: Rectangle, border_lines: List[Rectangle]) -> Optional[Rectangle]:
    for line in border_lines:
        if (intersection := rect.intersect(line)) is not None:
            return intersection
    return None

def split_free_blocks(free_blocks: List[Rectangle], line: Rectangle) -> List[Rectangle]:
    new_free_blocks = []
    for block in free_blocks:
        intersection = block.intersect(line)
        if intersection is None:
            new_free_blocks.append(block)
        else:
            new_free_blocks.extend(block.split(intersection))
    return new_free_blocks

def find_neighbors(rec: Rectangle, free_blocks: List[Rectangle]) -> Set[Rectangle]:
    neighbors = set()
    for border in rec.surrounding_borders:
        for block in free_blocks:
            if block.intersect(border):
                neighbors.add(block)
    return neighbors

def is_outside(rec: Rectangle, x_start: int, y_start: int, x_end: int, y_end: int) -> bool:
    return rec.x_start <= x_start or rec.y_start <= y_start or rec.x_end >= x_end or rec.y_end >= y_end

def classify_blocks(free_blocks: List[Rectangle], border_lines: List[Rectangle], x_start: int, y_start: int, x_end: int, y_end: int):
    outside, inside = set(), set()

    def check_for_outside(pos: Rectangle):
        agenda = deque([pos])
        visiting = {pos}
        is_external = False

        while agenda:
            current = agenda.popleft()
            
            if current in outside or is_outside(current, x_start, y_start, x_end, y_end):
                is_external = True
                break
            if current in inside:
                break

            for neighbor in find_neighbors(current, free_blocks):
                if neighbor in border_lines or neighbor in visiting:
                    continue
                visiting.add(neighbor)
                agenda.append(neighbor)

        if is_external:
            outside.update(visiting)
        else:
            inside.update(visiting)

    for block in free_blocks:
        check_for_outside(block)
    
    return outside, inside

def gen_border_lines(data, parse_func):
    pos = (0,0)
    border_lines : list[Rectangle]= list()
    for line in data:
        
        d,n = parse_func(line)
        start = tuple_add(pos, dir_to_diff[d]) 
        diff = tuple_mul(dir_to_diff[d], (n -1,n -1))
        
        
        end = tuple_add(start, diff) 
        r = Rectangle(x_start=min(start[0], end[0]), x_end=max(start[0], end[0]), y_start=min(start[1], end[1]), y_end=max(start[1], end[1]))
        border_lines.append(r)
        pos = end
    return border_lines
    
if __name__ == "__main__":
    
    
    data = get_aoc_input(18,2023).splitlines()
    keys = list(dir_to_diff)

    
    # part 1
    def parse_func(line):
        d, n, c = line.split()
        n = int(n)
        return d,n    
    
    res = get_solution(gen_border_lines(data, parse_func))
    print("Part 1", res)


    # part 2
    def parse_func(line):
        d, on, c = line.split()
        c = c.strip("()#")
        n = int(c[0:5], 16)
        d = keys[int(c[-1])]
        return d,n    
    
    res = get_solution(gen_border_lines(data, parse_func))
    print("Part 2", res)