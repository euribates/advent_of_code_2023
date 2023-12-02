#!/usr/bin/env python3

import sys
from rich import print
from core import parser


def get_bare_minimun(game):
    min_red = max([play.red for play in game.plays])
    min_green = max([play.green for play in game.plays])
    min_blue = max([play.blue for play in game.plays])
    return (min_red, min_green, min_blue)


def main(tron=True):
    filename = sys.argv[1]
    acc = 0
    for line in open(filename):
        game = parser(line)
        min_red, min_green, min_blue = get_bare_minimun(game)
        if tron:
            print(
                f'Game {game.num} needs'
                f' {min_red} red cubes,'
                f' {min_green} green cubes,'
                f' {min_blue} blue cubes'
                f' power is [bold]{min_red*min_green*min_blue}'
                )
        acc += min_red*min_green*min_blue
    print('Sol. part 2:', acc)


if __name__ == "__main__":
    main()
