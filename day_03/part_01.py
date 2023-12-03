#!/usr/bin/env python3

import sys

from core import load_lines, get_frontier, load_parts_and_symbols


def validate_part(col, row, parts, symbols):
    for (_col, _row) in get_frontier(col, row, parts):
        if (_col, _row) in symbols:
            return parts[col, row]
    return 0


def main():
    filename = sys.argv[1]
    _cols, _rows, lines = load_lines(filename)
    parts, symbols = load_parts_and_symbols(lines)
    acc = 0
    for pos, part in parts.items():
        col, row = pos
        acc += validate_part(col, row, parts, symbols)
    print(f'Sol. part one: {acc}')


if __name__ == "__main__":
    main()
