#!/usr/bin/env python3

from itertools import permutations
from core import get_options, load_input


def main(options):
    stars = load_input(options.filename)
    print(stars)
    stars.expand_universe()
    print(stars)
    acc = 0
    for a, b in permutations(stars.kernel.values(), 2):
        if a >= b:
            continue
        acc += a.distance(b)
    print(f'[Day 11] Sol. part one is: {acc}')


if __name__ == '__main__':
    options = get_options()
    main(options)
