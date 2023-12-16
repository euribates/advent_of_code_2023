#!/usr/bin/env python3

import sys

import core

NORTH = '↑'
EAST = '→'
SOUTH = '↓'
WEST = '←'


def first_move(plan, x, y):
    if plan.can_move_north(x, y):
        return NORTH, x, y - 1
    elif plan.can_move_east(x, y):
        return EAST, x + 1, y
    elif plan.can_move_south(x, y):
        return SOUTH, x, y + 1
    elif plan.can_move_west(x, y):
        return WEST, x - 1, y


def new_move(plan, orientation, x, y):
    char = plan[x, y]
    match orientation, char:
        case '↑', '|':
            y = y - 1
        case '↑', '7':
            x = x - 1
            orientation = '←'
        case '↑', 'F':
            x = x + 1
            orientation = '→'
        case '↓', '|':
            y = y + 1
        case '↓', 'J':
            x = x - 1
            orientation = '←'
        case '↓', 'L':
            x = x + 1
            orientation = '→'
        case '←', '-':
            x = x - 1
        case '←', 'L':
            y = y - 1
            orientation = '↑'
        case '←', 'F':
            y = y + 1
            orientation = '↓'
        case '→', '-':
            x = x + 1
        case '→', '7':
            y = y + 1
            orientation = '↓'
        case '→', 'J':
            y = y - 1
            orientation = '↑'
        case _:
            raise ValueError(f'x={x} y={y} Orientation={orientation} char={char}')
    return orientation, x, y


def main():
    filename = sys.argv[1]
    plan = core.load_input(filename)
    assert plan[plan.start_x, plan.start_y] == 'S'
    print(plan)
    steps = 0
    print(f"[{steps}] From {plan.start_x}, {plan.start_y}", end=' ')
    orientation, x, y = first_move(plan, plan.start_x, plan.start_y)
    print(f"move {orientation} to {x}, {y}")
    while plan[x, y] != 'S':
        steps += 1
        print(f"[{steps}] {plan[x, y]} From {x}, {y} move {orientation}", end=' ')
        orientation, x, y = new_move(plan, orientation, x, y)
        print(f"to {x}, {y}, new orientation is {orientation}")
    sol = (steps + 1) // 2
    print(f"Sol. part one: {sol}")

if __name__ == "__main__":
    main()








