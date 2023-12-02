#!/usr/bin/env python3

import sys


def load_input(filename):
    for line in open(filename, 'r'):
        yield line


def get_two_digits_number(line):
    buff = []
    for c in line:
        if c.isdigit():
            buff.append(c)
    return int(f'{buff[0]}{buff[-1]}')


assert get_two_digits_number('1abc2') == 12
assert get_two_digits_number('pqr3stu8vwx') == 38
assert get_two_digits_number('a1b2c3d4e5f') == 15
assert get_two_digits_number('treb7uchet') == 77


def sol_01(filename):
    return sum([
        get_two_digits_number(line)
        for line in load_input(filename)
        ])


assert sol_01('sample') == 142


def main():
    filename = sys.argv[1]
    print('Solution part 1:', sol_01(filename))


if __name__ == "__main__":
    main()


