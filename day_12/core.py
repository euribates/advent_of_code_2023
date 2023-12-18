#!/usr/bin/env python3

import argparse
from itertools import product


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 12')
    parser.add_argument('filename')
    parser.add_argument('-t', '--trace', action='store_true')
    return parser.parse_args()


def load_input(filename: str):
    with open(filename) as f_input:
        for line in f_input:
            yield line


def expand(record='.??..??...?##.',groups=(1, 1, 3)):
    unknowns = record.count('?')
    template = record.replace('?', '{}')
    for option in product('.#', repeat=unknowns):
        yield template.format(*option)

