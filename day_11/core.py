#!/usr/bin/env python3

import argparse
import dataclasses
from collections import defaultdict


def red(msg):
    return f"\u001b[31m{msg}\u001b[0m"


def green(msg):
    return f"\u001b[32m{msg}\u001b[0m"


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 11')
    parser.add_argument('filename')
    parser.add_argument('-t', '--trace', action='store_true')
    return parser.parse_args()


@dataclasses.dataclass(order=True)
class Vector2:
    x: int = 0
    y: int = 0

    def distance(self, other):
        return (
            abs(other.x - self.x) +
            abs(other.y - self.y)
            )



class StarMap:

    def __init__(self, filename):
        with open(filename, 'r') as f_input:
            lines = [line.strip() for line in f_input]
        self.width = len(lines[0])
        self.height = len(lines)
        self.kernel = {}
        self.stars_by_column = [0] * self.width
        self.stars_by_row = [0] * self.height
        self.num_stars = 0
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == '#':
                    self.stars_by_column[x] += 1
                    self.stars_by_row[y] += 1
                    self.num_stars += 1
                    self.kernel[x, y] = Vector2(x, y)
    
    def get_col_expands(self):
        return [
            index
            for index, value in enumerate(self.stars_by_column)
            if value == 0
            ]

    def get_row_expands(self):
        return [
            index
            for index, value in enumerate(self.stars_by_row)
            if value == 0
            ]

    def expand_universe(self):
        for x_frontier in reversed(self.get_col_expands()):
            wave = []
            for (x, y) in self.kernel:
                if x > x_frontier:
                    star = self.kernel[x, y]
                    wave.append(star)
            for star in wave:
                del self.kernel[star.x, star.y]
                star.x += 1
                self.kernel[star.x, star.y] = star
            print(self.stars_by_column)
            self.stars_by_column.insert(x_frontier, 0)
            self.width += 1
        for y_frontier in reversed(self.get_row_expands()):
            wave = []
            for (x, y) in self.kernel:
                if y > y_frontier:
                    star = self.kernel[x, y]
                    wave.append(star)
            for star in wave:
                del self.kernel[star.x, star.y]
                star.y += 1
                self.kernel[star.x, star.y] = star
            self.stars_by_row.insert(y_frontier, 0)
            self.height += 1

    def is_full_empty(self, x, y):
        return self.stars_by_column[x] == 0 or self.stars_by_row[y] == 0

    def __str__(self):
        buff = ['      ']
        for x in range(self.width):
            buff.append(f'{x:^3}')
        buff.append('\n')
        buff.append('      ')
        for x in range(self.width):
            n_stars = self.stars_by_column[x]
            if n_stars:
                buff.append(f'{n_stars:^3}')
            else:
                buff.append('░░░')
        buff.append('\n')
        for y in range(self.height):
            buff.append(f'{y:^3}')
            n_stars = self.stars_by_row[y]
            if n_stars:
                buff.append(f'{n_stars:^3}')
            else:
                buff.append('░░░')
            for x in range(self.width):
                if self.is_full_empty(x, y):
                    buff.append('░░░')
                elif (x, y) in self.kernel:
                    #  star = self.kernel[x, y]
                    buff.append(green(' ★ '))
                else:
                    buff.append('   ')
            buff.append('\n')
        return ''.join(buff)

def load_input(filename: str):
    return StarMap(filename)
