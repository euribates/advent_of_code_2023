#!/usr/bin/env python3

import argparse


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 13')
    parser.add_argument('filename')
    parser.add_argument('-t', '--trace', action='store_true')
    return parser.parse_args()


def load_input(filename: str):
    with open(filename) as f_input:
        buff = []
        for line in f_input:
            line = line.strip()
            if line:
                buff.append(line)
            else:
                yield buff.copy()
                buff = []
        yield buff




def transpose(plan):
    return list(map(lambda _: ''.join(_), zip(*plan)))


