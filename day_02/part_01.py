#!/usr/bin/env python3

import sys
from rich import print
from core import parser


def pass_limits(game, max_red, max_green, max_blue):
    for play in game.plays:
        if play.red > max_red:
            return True
        if play.green > max_green:
            return True
        if play.blue > max_blue:
            return True
    return False


def main(tron=True):
    filename = sys.argv[1]
    acc = 0
    for line in open(filename):
        game = parser(line)
        if pass_limits(game, max_red=12, max_green=13, max_blue=14):
            print(f'[red] Game {game.num} DO NOT pass')
        else:
            print(f'[green] Game {game.num} pass')
            acc += game.num
    print('Sol. part 1:', acc)


if __name__ == "__main__":
    main()
