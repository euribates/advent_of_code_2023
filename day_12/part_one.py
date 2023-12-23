#!/usr/bin/env python3

from core import get_options, load_input
from core import count_valid_expansions


def main(options):
    acc = 0
    for record, damaged_parts in load_input(options.filename):
        valid_count = count_valid_expansions(record, damaged_parts)
        print(record, valid_count)
        acc += valid_count
    print(f'[Day 12] Sol. part one is: {acc}')


if __name__ == '__main__':
    options = get_options()
    main(options)
