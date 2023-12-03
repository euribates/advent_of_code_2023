#!/usr/bin/env python3

import sys
from collections import defaultdict
from functools import reduce
import operator

from core import load_lines, get_frontier, load_parts_and_symbols


def find_gears(parts, symbols):
    gears = defaultdict(set)
    for (col, row), part in parts.items():
        for _col, _row in get_frontier(col, row, parts):
            if (_col, _row) in symbols and symbols[_col, _row] == '*':
                gears[_col, _row].add(tuple([col, row, part]))
    return gears


def main():
    filename = sys.argv[1]
    _cols, _rows, lines = load_lines(filename)
    parts, symbols = load_parts_and_symbols(lines)
    gears = find_gears(parts, symbols)
    sol = 0
    for _pos, parts_set in gears.items():
        if len(parts_set) == 2:
            sol += reduce(operator.mul, [_[2] for _ in parts_set], 1)
    print(f'Sol. part two: {sol}')


if __name__ == "__main__":
    main()
