from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from typing import Callable
import re
colorama_init()

def tuple_add(one : tuple, two : tuple):
    return tuple(a+b for a,b in zip(one,two))


def tuple_mul(one : tuple, two : tuple):
    return tuple(a*b for a,b in zip(one,two))

def tuple_sub(one : tuple, two : tuple):
    return tuple(a-b for a,b in zip(one,two))


def highlight(s, color : str):
    assert hasattr(Fore, color), "Color does not exist"

    return f"{getattr(Fore,color)}{s}{Style.RESET_ALL}"


def extract_ints(s : str) -> list[int]:
    return list(map(int, re.findall(r"\d+", s)))

def get_2dmap(data : list[str], filter_func : Callable = lambda x: True, transform : Callable = lambda x : x):
    return {(x, y): transform(c) for y, line in enumerate(data) for x, c in enumerate(line) if filter_func(transform)}

