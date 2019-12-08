import os
from typing import List

HALT_CODE = '99'

operators = {
    '1': lambda left, right: left + right,
    '2': lambda left, right: left * right,
    '3': lambda: input("provide input: "),
    '4': lambda value: print(value),
}


def contains_parameter_modes(opcode: str) -> bool:
    suffixes = [f'0{i}' for i in range(1, 9)]
    return any(opcode.endswith(suffix) for suffix in suffixes)


def get_params(intcodes, params, modes):
    modes = list(reversed(modes))
    params_to_instruction = []
    for i in range(len(params) - 1):
        try:
            mode = modes[i]
        except IndexError:
            mode = '0'

        param = int(params[i])
        if mode == '1':
            params_to_instruction.append(param)
        else:
            params_to_instruction.append(int(intcodes[param]))

    output_param = int(params[len(params) - 1])
    return params_to_instruction + [output_param]


def get_param(intcodes, param, modes):
    out = param
    if modes and modes[0] == '0':
        out = int(intcodes[param])
    return int(out)


def part_1(intcodes: List[str]) -> List[str]:
    addr = 0
    while (opcode := intcodes[addr]) != HALT_CODE:
        addr = evaluate(intcodes)(opcode, addr)
    return intcodes


def strip_modes(opcode):
    return opcode[len(opcode) - 1], list(opcode[:len(opcode) - 2])


def evaluate(intcodes: List[str]):
    def run(opcode: str, addr: int):
        modes = []
        print(intcodes, addr)
        if contains_parameter_modes(opcode):
            opcode, modes = strip_modes(opcode)

        if opcode in ['3', '4']:
            out = get_param(intcodes, intcodes[addr + 1], modes)
            if opcode == '3':
                intcodes[out] = operators[opcode]()
            elif opcode == '4':
                operators[opcode](intcodes[out])
            addr += 2
        else:
            x, y, out = get_params(intcodes, intcodes[addr + 1: addr + 4], modes)
            if opcode in ['1', '2']:
                intcodes[out] = str(operators[opcode](x, y))
                addr += 4
            elif opcode == '5':
                if x != 0:
                    addr = y
                else:
                    addr += 3
            elif opcode == '6':
                if x == 0:
                    addr = y
                else:
                    addr += 3
            elif opcode == '7':
                if x < y:
                    intcodes[out] = '1'
                else:
                    intcodes[out] = '0'
                addr += 4
            elif opcode == '8':
                if x == y:
                    intcodes[out] = '1'
                else:
                    intcodes[out] = '0'
                addr += 4
        return addr
    return run


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    file = f.read()
    file = [x for x in file.strip().split(sep=',')]
    print(",".join(part_1(file)))
