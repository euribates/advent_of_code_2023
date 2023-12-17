
#!/usr/bin/env python3

from itertools import permutations
from core import get_options, load_input


def main(options):
    stars = load_input(options.filename)
    stars.expand_universe(options.gap)
    acc = 0
    for a, b in permutations(stars.kernel.values(), 2):
        if a >= b:
            continue
        acc += a.distance(b)
    print(f'[Day 11] Sol. part two is: {acc}')


if __name__ == '__main__':
    options = get_options()
    main(options)
