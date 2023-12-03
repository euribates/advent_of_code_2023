#!/usr/bin/env python3

from core import process_line
from core import load_lines
from core import load_parts_and_symbols
from core import get_frontier


SAMPLE = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..',
    ]


def test_load_lines():
    cols, rows, lines = load_lines('sample')
    assert cols == 10
    assert rows == 10
    assert lines == SAMPLE


def test_process_line_zero():
    line = '467..114..'
    parts, symbols = process_line(0, line)
    assert parts == {
        (0, 0): 467,
        (5, 0): 114,
        }
    assert symbols == {}


def test_process_line_one():
    line = '...*......'
    parts, symbols = process_line(1, line)
    assert parts == {}
    assert symbols == {
        (3, 1): '*',
        }


def test_process_line_four():
    line = '617*......'
    parts, symbols = process_line(4, line)
    assert parts == {
        (0, 4): 617,
        }
    assert symbols == {
        (3, 4): '*',
        }

def test_process_line_part_at_end():
    line = '......*617'
    parts, symbols = process_line(4, line)
    assert parts == {
        (7, 4): 617,
        }
    assert symbols == {
        (6, 4): '*',
        }

def test_process_line_two_parts_separated_by_symbol():
    line = '.585*312.'
    parts, symbols = process_line(134, line)
    assert parts == {
        (1, 134): 585,
        (5, 134): 312
        }
    assert symbols == {
        (4, 134): '*',
        }


def test_process_line_two_134():
    line = '...5.88.*...'
    parts, symbols = process_line(0, line)
    assert parts == {
        (3, 0): 5,
        (5, 0): 88
        }
    assert symbols == {
        (8, 0): '*',
        }


def test_load_parts_and_symbols():
    lines = [
        '...#.',
        '12...',
        '.34.*',
        ]
    parts, symbols = load_parts_and_symbols(lines, tron=True)
    assert parts == {
        (0, 1): 12,
        (1, 2): 34,
        }
    assert symbols == {
        (3, 0): '#',
        (4, 2): '*',
        }


def test_get_frontier():
    parts = {
        (0, 0): 234
        }
    frontier = list(get_frontier(0, 0, parts))
    assert len(frontier) == 12
    assert frontier[0] == (-1, -1)
    assert frontier[1] == (0, -1)
    assert frontier[2] == (1, -1)
    assert frontier[3] == (2, -1)
    assert frontier[4] == (3, -1)
    assert frontier[5] == (-1, 0)
    assert frontier[6] == (3, 0)
    assert frontier[7] == (-1, 1)
    assert frontier[8] == (0, 1)
    assert frontier[9] == (1, 1)
    assert frontier[10] == (2, 1)
    assert frontier[11] == (3, 1)
