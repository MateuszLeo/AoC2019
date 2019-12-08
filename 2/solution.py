import os
from typing import List, Tuple

operators = {
    1: lambda left, right: left + right,
    2: lambda left, right: left * right,
}


def part_1(intcodes: List[int], noun: int = 12, verb: int = 2) -> int:
    addr = 0
    intcodes[1] = noun
    intcodes[2] = verb

    while (operator := operators.get(intcodes[addr], None)) is not None:
        x, y, out = intcodes[addr + 1: addr + 4]
        intcodes[out] = operator(intcodes[x], intcodes[y])
        addr += 4
    return intcodes[0]


def part_2(intcodes: List[int]) -> Tuple[int, int]:
    value = 19690720
    for n in range(12, 100):
        for n2 in range(2, 100):
            if part_1(intcodes[:], n, n2) == value:
                return n, n2


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    content = f.read()
    intcodes = [int(v) for v in content.split(sep=",")]
    print("part 1", part_1(intcodes[:]))
    print("part 2", part_2(intcodes[:]))
