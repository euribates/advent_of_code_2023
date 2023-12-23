#!/usr/bin/env python3

import argparse
import re
from itertools import product


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 12')
    parser.add_argument('filename')
    parser.add_argument('-t', '--trace', action='store_true')
    return parser.parse_args()


def load_input(filename: str):
    with open(filename) as f_input:
        for line in f_input:
            line = line.strip()
            record, rest = line.split(' ')
            groups = tuple([
                int(_)
                for _ in rest.split(',')
                ])
            yield record, groups


def expand(record, groups):
    unknowns = record.count('?')
    template = record.replace('?', '{}')
    for option in product('.#', repeat=unknowns):
        yield template.format(*option)


pat_hashes = re.compile(r'#+')


def find_groups(record):
    return tuple([
        len(part)
        for part in pat_hashes.findall(record)
        ])


def count_valid_expansions(record, groups):
    acc = 0
    for expanded in expand(record, groups):
        if find_groups(expanded) == groups:
            acc += 1
    return acc
