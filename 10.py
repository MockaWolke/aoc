from aoc import get_aoc_input
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from functools import reduce

colorama_init()

data = get_aoc_input(day=10, year=2023)
# Your solution starts here


f = lambda a, b: (a[0] + b[0], a[1] + b[1])

meaning = {
    "|": ((0, 1), (0, -1)),
    "-": ((1, 0), (-1, 0)),
    "L": ((1, 0), (0, -1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((-1, 0), (0, 1)),
    "F": ((0, 1), (1, 0)),
}

cords = {
    (x, y): char
    for y, line in enumerate(data.splitlines())
    for x, char in enumerate(line)
}
start = [a for a, b in cords.items() if b == "S"][0]


def single_loop(start_move, start):
    pos = start
    move = start_move
    last = None

    i = 0
    history = {}

    while True:

        # save
        last = pos
        history[pos] = i
        i += 1

        # do move
        pos = f(pos, move)

        # checl validity
        if pos not in cords or (char := cords[pos]) not in meaning:
            break

        # new move
        one, two = meaning[char]
        if f(pos, one) == last:
            move = two
        else:
            move = one

    del history[start]

    return history, cords.get(pos) == "S"


def check_for_loop(symbol: str):

    left, right = meaning[symbol]

    h1, w1 = single_loop(left, start)
    h2, w2 = single_loop(right, start)

    if w1 and w2 and len(h1) == len(h2):

        for a, b in zip(h1, reversed(h2)):
            if a != b:
                return False
        return len(h1) // 2 + 1, list(h1)

    return None


def get_corners_position(pos):

    corners = []
    for xv in [-1, 1]:
        for yv in [-1, 1]:
            l = [
                f(pos, (0, 0)),
                f(pos, (xv, 0)),
                f(pos, (xv, yv)),
                f(pos, (0, yv)),
            ]

            l.sort(key=lambda x: x[0] * 10 + x[1])
            corners.append(tuple(l))
    return corners


def symmetric(func):
    def new_func(a, b):
        return func(a, b) and func(b, a)

    return new_func


@symmetric
def check_blockade(pos1, pos2):
    moves = meaning.get(cords.get(pos1))
    if moves is None:
        return False
    for diff in moves:
        if f(pos1, diff) == pos2:
            return True
    return False


def get_valid_transitions(corner):

    top_left, bottom_left, top_right, bottom_right = corner

    valid = []
    if not check_blockade(top_left, bottom_left):
        valid.append((-1, 0))
    if not check_blockade(top_left, top_right):
        valid.append((0, -1))
    if not check_blockade(bottom_right, top_right):
        valid.append((1, 0))
    if not check_blockade(bottom_right, bottom_left):
        valid.append((0, 1))

    valid = [tuple(map(lambda x: f(x, v), corner)) for v in valid]
    return valid


true_corners = set()
false_corners = set()
is_out = lambda x: any(c not in cords for c in x)


def recu_check_entry(corner):
    history = set()

    val = recu_check(corner, history)

    if val:
        true_corners.update(history)
    else:
        false_corners.update(history)

    return val


def recu_check(corner, history: set):

    if corner in false_corners:
        return False
    if corner in true_corners:
        return True

    if is_out(corner):
        true_corners.add(corner)
        return True

    history.add(corner)
    for new_corner in get_valid_transitions(corner):

        if new_corner not in history and recu_check(new_corner, history):
            true_corners.add(corner)

            return True
    return False


for symbol in meaning:
    if (val := check_for_loop(symbol=symbol)) is not None:
        print(val[0])
        break

cords[start] = symbol
loop = set([start] + val[1])


enclosed = set()


def check_dot(pos):

    for corner in get_corners_position(pos):

        if recu_check_entry(corner):
            return True

    return False


for y, line in enumerate(data.splitlines()):

    s = ""
    for x, char in enumerate(line):
        if (x, y) in loop:
            s += f"{Fore.GREEN}{char}{Style.RESET_ALL}"
        elif not check_dot((x, y)):
            enclosed.add((x, y))
            s += f"{Fore.RED}{char}{Style.RESET_ALL}"
        else:
            s += char

    print(s)


print("\nPart1:", len(loop)//2, "Part2: ",len(enclosed))
