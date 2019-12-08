import os
from typing import List

central_point = (0, 0)

Wires = List[List[str]]


def get_values(direction: str, coord, value):
    if direction in ["U", "R"]:
        n = coord + value
        return n, range(coord, n)
    n = coord - value
    return n, range(n, coord)


def make_grid(wires: Wires):
    for wire in wires:
        x, y = central_point
        grid = {}
        step = 0
        for path in wire:
            direction, value = path[:1], int(path[1:])
            if direction in ["D", "U"]:
                next_y, r = get_values(direction, y, value)
                for i in r:
                    key = (x, i)
                    if key not in grid:
                        grid[key] = step
                    step += 1
                y = next_y
            else:
                next_x, r = get_values(direction, x, value)
                for i in r:
                    key = (i, y)
                    if key not in grid:
                        grid[key] = step
                    step += 1
                x = next_x

        # remove central point
        if central_point in grid.keys():
            grid.pop(key)
        yield grid


def get_intersection(wires: Wires):
    grid_1, grid_2 = make_grid(wires)
    intersection = set(grid_1.keys()).intersection(set(grid_2.keys()))
    return intersection


def part_1(wires: Wires) -> int:
    intersection = get_intersection(wires)
    q1, q2 = central_point

    distance = []
    for k in intersection:
        p1, p2 = k
        result = abs(q1 - p1) + abs(q2 - p2)
        if result != 0:
            distance.append(result)
    return min(distance)


def part_2(wires: Wires):
    grid_1, grid_2 = make_grid(wires)
    intersection = get_intersection(wires)
    x = []
    for i in intersection:
        v = grid_1[i] + grid_2[i]
        if v > 0:
            x.append(v)
    return min(x)


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = f.readlines()
    lines = [line.strip().split(sep=",") for line in lines]
    print(part_1(lines))
