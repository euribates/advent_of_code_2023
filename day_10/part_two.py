#!/usr/bin/env python3

import sys

import core

def red(msg):
    return f"\u001b[31m{msg}\u001b[0m"


def green(msg):
    return f"\u001b[32m{msg}\u001b[0m"


def is_inside(plan, perimeter, x, y, tron=False):
    if tron:
        print(f"\n{x=}, {y=}", end=' ')
    if (x, y) in perimeter:
        if tron:
            print(f"{x}, {y} forma parte del perímetro")
        return False
    counter = 0
    prev = None
    if tron:
        print()
    for _x in range(0, x):
        char = plan[_x, y]
        if tron:
            print(f"{_x=}, {y=} [{char}] prev is {prev} {counter=}", end=' ')
        if (_x, y) in perimeter:
            char = plan[_x, y]
            if char == '|':
                if tron:
                    print(" (+1)", end='')
                prev = None
                counter += 1
            elif char == 'J' and prev == 'F':
                prev = None
                counter += 1
            elif char == '7' and prev == 'L':
                prev = None
                counter += 1
            elif char != '-':
                prev = char
        if tron:
            print()
    if tron:
        print(f'Final counter is {counter}')
    return counter % 2


def print_perimeter(plan, perimeter):
    buff = [f'Plan size is {plan.max_x} x {plan.max_y}:\n']
    for y in range(plan.max_y):
        for x in range(plan.max_x):
            if (x, y) in perimeter:

                m = core.CHAR_TO_TILE_MAP[plan[x, y]]
                buff.append(green(m))
            else:
                if inside := is_inside(plan, perimeter, x, y):
                    # buff.append(green('▒'))
                    buff.append(green(inside))
                else:
                    buff.append(red(inside))
        buff.append('\n')
    return ''.join(buff)


def main():
    filename = sys.argv[1]
    plan = core.load_input(filename)
    perimeter = list(core.get_perimeter(plan))
    plan.replace_start()
    # print(is_inside(plan, perimeter, 20, 3, tron=True))
    # print(is_inside(plan, perimeter, 1, 6))
    # print(is_inside(plan, perimeter, 2, 6, tron=True))
    # print(is_inside(plan, perimeter, 3, 6))
    # print(is_inside(plan, perimeter, 4, 7))
    # print(is_inside(plan, perimeter, 5, 7))
    print(print_perimeter(plan, perimeter))
    acc = 0
    for y in range(plan.max_y):
        for x in range(plan.max_x):
            if is_inside(plan, perimeter, x, y):
                acc += 1
    print(f'acc: {acc}')


if __name__ == "__main__":
    main()








