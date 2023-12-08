#!/usr/bin/env python3

import sys
import math
from itertools import cycle

from core import load_input


def follow_route(start, targets, instructions, kernel):
    current = start
    instructions = cycle(instructions)
    counter = 0
    while True:
        ins = next(instructions)
        current = kernel[current][ins]
        counter += 1
        if current.endswith('Z'):
            yield current, counter


def main():
    filename = sys.argv[1]
    instructions, kernel = load_input(filename)
    starts = list({key for key in kernel if key.endswith('A')})
    ends_right = {_['R'] for _ in kernel.values() if _['R'].endswith('Z')}
    ends_left = {_['L'] for _ in kernel.values() if _['L'].endswith('Z')}
    targets = tuple(ends_right | ends_left)
    tasks = {
         start: follow_route(start, targets, instructions, kernel)
         for start in starts
         }
    counters = {start: 0 for start in starts}
    for start in starts:
        _state, counter = next(tasks[start])
        counters[start] = counter
        # print(f'start {start}: in state {state} after {counter} steps')
    values = list(counters.values())
    sol = math.lcm(*values)
    print(f"Sol. part two: {sol}")


if __name__ == "__main__":
    main()
