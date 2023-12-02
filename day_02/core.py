#!/usr/bin/env python3

import dataclasses
import re


sep = re.compile(r'([;:])')


def split_items(line):
    for item in sep.split(line):
        yield item.strip()


@dataclasses.dataclass
class Play:
    red: int = 0
    green: int = 0
    blue: int = 0

    def __init__(self, s):
        values = s.split(', ')
        for value in values:
            num, color = value.split(' ')
            match color:
                case 'red':
                    self.red = int(num)
                case 'green':
                    self.green = int(num)
                case 'blue':
                    self.blue = int(num)


@dataclasses.dataclass
class Game:
    num: int = None
    plays: list[Play] = dataclasses.field(default_factory=list)

    pat = re.compile(r'Game (\d+)')

    def __init__(self, token):
        match = self.pat.match(token)
        self.num = int(match.group(1))
        self.plays = []


def parser(line):
    tokens = list(split_items(line))
    first_token = tokens.pop(0)
    game = Game(first_token)
    assert tokens.pop(0) == ':'
    while tokens:
        play = tokens.pop(0)
        game.plays.append(Play(play))
        if tokens:
            assert tokens.pop(0) == ';'
    return game
