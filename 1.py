import re
from aoc.get_data import get_aoc_input


lines = get_aoc_input(1, 2023).splitlines()

val = 0

for line in lines:

    numbers = re.findall(r"\d", line)

    val += int(numbers[0] + numbers[-1])

print(val)


dic = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

val = 0

for line in lines:
    for number, v in dic.items():
        line = line.replace(number, number +str(v) + number)
    numbers = re.findall("\d", line)
    num = int(numbers[0] + numbers[-1])
    val += num
print(val)