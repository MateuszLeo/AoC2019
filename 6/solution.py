import os
import collections

from typing import List


def get_maping(orbits_map: List[str]):
    mapping = collections.defaultdict(set)
    for orbit in orbits_map:
        _from, _to = orbit.split(sep=')')
        mapping[_from].add(_to)
    return mapping


def get_paths(mapping):
    def search(orbit, path):
        for parent, orbits in mapping.items():
            if orbit == parent:
                continue
            if orbit in orbits:
                path.append(parent)
                search(parent, path)
        return path

    paths = {}
    for parent, orbits in mapping.items():
        for orbit in orbits:
            paths[orbit] = search(parent, [parent])
    return paths


def part_1(paths):
    return sum([len(v) for v in paths.values()])


def part_2(paths):
    you, san = list(reversed(paths['YOU'])), list(reversed(paths['SAN']))
    for i, (x, y) in enumerate(zip(you, san)):
        if x != y:
            return len(you) - i + len(san) - i


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    mapping = get_maping(lines)
    paths = get_paths(mapping)

    print(part_1(paths))
    print(part_2(paths))
