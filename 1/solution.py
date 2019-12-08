import os
import math


def part_1(mass: int) -> int:
    return math.trunc(mass / 3) - 2


def part_2(mass: int, result=0) -> int:
    value = part_1(mass)
    if value <= 0:
        return result
    return part_2(value, value + result)


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = f.readlines()
    p_1 = sum(part_1(int(line)) for line in lines)
    p_2 = sum(part_2(int(line)) for line in lines)
    print("part_1", p_1)
    print("part_2", p_2)
