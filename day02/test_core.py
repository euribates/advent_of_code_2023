#!/usr/bin/env python3

from core import sep
from core import split_items
from core import Play
from core import Game
from core import parser


SAMPLE_ONE = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
SAMPLE_TWO = 'Game 1: 7 blue, 4 red, 11 green; 2 red, 2 blue, 7 green; 2 red, 13 blue, 8 green; 18 blue, 7 green, 5 red'


def test_reg_expp():
    assert sep.split(SAMPLE_ONE) == [
        'Game 1', ':',
        ' 3 blue, 4 red', ';',
        ' 1 red, 2 green, 6 blue', ';',
        ' 2 green',
        ]
    assert sep.split(SAMPLE_TWO) == [
        'Game 1', ':',
        ' 7 blue, 4 red, 11 green', ';',
        ' 2 red, 2 blue, 7 green', ';',
        ' 2 red, 13 blue, 8 green', ';',
        ' 18 blue, 7 green, 5 red',
        ]


def test_split_items():
    assert list(split_items(SAMPLE_ONE)) == [
        'Game 1', ':',
        '3 blue, 4 red', ';',
        '1 red, 2 green, 6 blue', ';',
        '2 green',
    ]
    assert list(split_items(SAMPLE_TWO)) == [
        'Game 1', ':',
        '7 blue, 4 red, 11 green', ';',
        '2 red, 2 blue, 7 green', ';',
        '2 red, 13 blue, 8 green', ';',
        '18 blue, 7 green, 5 red',
        ]


def test_play():
    p = Play('23 red, 1 green')
    assert p.red == 23
    assert p.green == 1
    assert p.blue == 0


def test_game():
    g = Game('Game 12')
    assert g.num == 12
    assert g.plays == []

    
def test_parser():
    g = parser(SAMPLE_ONE)
    assert g.num == 1
    assert len(g.plays) == 3
