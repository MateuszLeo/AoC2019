from typing import Tuple


def part_1(lower_bound: int, upper_bound: int) -> Tuple[int, set]:
    numbers = set()
    for n in range(lower_bound, upper_bound):
        string = str(n)
        string_list = list(string)
        if sorted(string_list) == string_list:
            for s in string:
                same = f"{s}{s}"
                if same in string:
                    numbers.add(n)
    return len(numbers), numbers


def part_2(lower_bound: int, upper_bound: int) -> int:
    _, part_1_numbers = part_1(lower_bound, upper_bound)

    numbers = set()
    for n in part_1_numbers:
        string = str(n)
        for char in string:
            if len("".join(string.split(sep=char))) == 4:
                numbers.add(n)

    return len(numbers)


_input = [357253, 892942]
print(part_1(*_input)[0])
print(part_2(*_input))

