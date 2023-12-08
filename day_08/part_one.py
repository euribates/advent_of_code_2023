#!/usr/bin/env python3

import sys
from itertools import cycle

from core import load_input


def main():
    filename = sys.argv[1]
    instructions, kernel = load_input(filename)
    start = 'AAA'
    target = 'ZZZ'
    current = start
    instructions = cycle(instructions)
    tope = len(kernel) ** 2
    counter = 0
    while current != target:
        ins = next(instructions)
        current = kernel[current][ins]
        counter += 1
        if counter > tope:
            break
    print(f"Sol. part one: {counter}")



if __name__ == "__main__":
    main()
