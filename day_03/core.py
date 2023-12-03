#!/usr/bin/env python3


def load_lines(filename):
    with open(filename, 'r') as f_in:
        lines = [_.strip() for _ in f_in.readlines() if _.strip()]
    cols = len(lines[0])
    rows = len(lines)
    return cols, rows, lines


def load_parts_and_symbols(lines, tron=False):
    parts = {}
    symbols = {}
    for row, line in enumerate(lines):
        new_parts, new_symbols = process_line(row, line)
        if tron:
            print(
                f'{line}'
                f' parts={len(new_parts)}'
                f' symbols={len(new_symbols)}'
                )
        parts.update(new_parts)
        symbols.update(new_symbols)
    return parts, symbols


def process_line(row, line):
    parts = {}
    symbols = {}
    chars = list(line); col = 0
    while chars:
        char = chars.pop(0); col += 1
        if char.isdigit():
            buff = []
            start = col - 1
            while chars and char.isdigit():
                buff.append(char)
                char = chars.pop(0); col += 1
            if char.isdigit():
                buff.append(char)
            else:  # Oops, we need to put char back
                chars.insert(0, char); col -= 1
            parts[(start, row)] = int(''.join(buff))
        elif char != '.':
            symbols[(col-1, row)] = char
    return parts, symbols


def get_frontier(col, row, parts):
    part = parts[col, row]
    width = len(str(part))
    for c in range(col-1, col + width + 1):
        yield c, row - 1
    yield col - 1, row
    # We do not need to check the symbol itself
    yield col + width, row
    for c in range(col-1, col + width + 1):
        yield c, row + 1


def print_map(cols, rows, parts, symbols):
    for row in range(rows):
        for col in range(cols):
            if (col, row) in symbols:
                print(symbols[col, row], end='')
            elif (col, row) in parts:
                print('■', end='')
            else:
                print('.', end='')
        print()
