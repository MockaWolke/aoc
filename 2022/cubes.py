direction_to_name = {0: "r", 1: "d", 2: "l", 3: "u"}
name_to_direction = dict(zip(direction_to_name.values(), direction_to_name.keys()))

test_cube = {}


test_cube[(2, 0)] = {
    "l": ((1, 1), "d", False),
    "u": ((0, 1), "d", True),
    "r": ((3, 2), "l", True),
}

test_cube[(1, 1)] = {
    "u": ((2, 0), "r", False),
    "d": ((2, 2), "r", True),
}

test_cube[(2, 1)] = {
    "r": ((3, 2), "d", True),
}

test_cube[(2, 2)] = {
    "d": ((0, 1), "u", True),
    "l": ((1, 1), "u", True),
}

test_cube[(0, 1)] = {
    "d": ((2, 2), "u", True),
    "l": ((3, 2), "u", True),
    "u": ((2, 0), "d", True),
}

test_cube[(3, 2)] = {
    "d": ((0, 1), "u", True),
    "r": ((2, 0), "l", True),
    "u": ((2, 1), "l", True),
}

real_cube = {}

real_cube[(1, 1)] = {
    "l": ((0, 2), "d", False),
    "r": ((2, 0), "u", False),
}

real_cube[(0, 2)] = {
    "u": ((1, 1), "r", False),
    "l": ((1, 0), "r", True),
}

real_cube[(1, 0)] = {
    "u": ((0, 3), "r", False), 
    "l": ((0, 2), "r", True),
}

real_cube[(0, 3)] = {
    "r": ((1, 2), "u", False),
    "l": ((1, 0), "d", False),  
    "d": ((2, 0), "d", False),  
}

real_cube[(1, 2)] = {
    "d": ((0, 3), "l", False),
    "r": ((2, 0), "l", True),  
}

real_cube[(2, 0)] = {
    "d": ((1, 1), "l", False),
    "r": ((1, 2), "l", True),  
    "u": ((0, 3), "u", False),  
}
