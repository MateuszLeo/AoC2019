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
    suffixes = [f'0{i}' for i in range(1, 5)]
    return any(opcode.endswith(suffix) for suffix in suffixes)


def part_1(intcodes: List[str]) -> List[str]:
    addr = 0
    while (opcode := intcodes[addr]) != HALT_CODE:
        if contains_parameter_modes(opcode):
            modes = list(opcode[:len(opcode) - 2])
            opcode = opcode[len(opcode) - 1]
            if opcode in ['1', '2']:
                params = intcodes[addr + 1: addr + 4]
                for i in range(3):
                    try:
                        modes[i]
                    except IndexError:
                        modes = ['0'] + modes

                modes = list(reversed(modes))
                params_to_instruction = []
                for i in range(3):
                    param = int(params[i])
                    mode = modes[i]
                    if i == 2 or mode == '1':
                        params_to_instruction.append(param)
                    else:
                        params_to_instruction.append(int(intcodes[param]))

                x, y, out = params_to_instruction
                intcodes[out] = str(operators[opcode](x, y))
                addr += 4
            else:
                param = intcodes[addr + 1]
                modes = list(reversed(modes))
                out = int(param)
                if modes[0] == '0':
                    out = int(intcodes[out])
                if opcode == '3':
                    intcodes[out] = operators[opcode]()
                else:
                    operators[opcode](intcodes[out])
                addr += 2
            continue
        addr = evaluate(intcodes)(opcode, addr)
    return intcodes


def evaluate(intcodes: List[str]):
    def run(opcode: str, addr: int):
        if opcode in ['1', '2']:
            x, y, out = [int(x) for x in intcodes[addr + 1: addr + 4]]
            intcodes[out] = str(operators[opcode](int(intcodes[x]), int(intcodes[y])))
            addr += 4
        elif opcode == '3':
            out = int(intcodes[addr + 1])
            intcodes[out] = operators[opcode]()
            addr += 2
        elif opcode == '4':
            out = int(intcodes[addr + 1])
            operators[opcode](intcodes[out])
            addr += 2
        return addr

    return run


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    file = f.read()
    file = [x for x in file.strip().split(sep=',')]
    print(",".join(part_1(file)))
    # print(part_1(['3', '0', '4', '0', '99']))
    # print(part_1(['1101', '100', '-1', '4', '0']))
    # print(part_1(['1002', '4', '3', '4', '33']))
