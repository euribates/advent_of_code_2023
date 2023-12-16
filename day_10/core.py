#!/usr/bin/env python3

NORTH = '↑'
EAST = '→'
SOUTH = '↓'
WEST = '←'

DELIMETERS = {'F', 'L', '|', '7', '-', 'J', 'S'}
H_DELIMETERS = DELIMETERS - {'-'}

CHAR_TO_TILE_MAP = {
    '.': ' ',
    'F': '┌',
    'L': '└',
    '-': '─',
    '|': '|',
    '7': '┐',
    'J': '┘',
    'S': '*',
    }


def as_tile(char):
    if char in CHAR_TO_TILE_MAP:
        return CHAR_TO_TILE_MAP[char]
    raise ValueError(f'Invalid character {char!r}')


class Plan:

    def __init__(self, lines):
        self.kernel = {}
        self.start_x = self.start_y = 0
        for y, line in enumerate(lines):
            line = line.strip()
            for x, char in enumerate(line):
                if char == 'S':
                    self.start_x = x
                    self.start_y = y
                self.kernel[x, y] = char
        self.max_x = x + 1
        self.max_y = y + 1
        
    def __str__(self):
        buff = [f'Plan size is {self.max_x} x {self.max_y}:\n']
        for y in range(self.max_y):
            for x in range(self.max_x):
                char = self.kernel[x, y]
                buff.append(as_tile(char))
            buff.append('\n')
        return ''.join(buff)

    def can_move_west(self, x, y):
        if x - 1 < 0:
            return False
        return self.kernel[x-1, y] in {'-', 'F', 'L'}

    def can_move_east(self, x, y):
        if x + 1 >= self.max_x:
            return False
        return self.kernel[x+1, y] in {'-', '7', 'J'}

    def can_move_north(self, x, y):
        if y-1 < 0:
            return False
        return self.kernel[x, y-1] in {'|', '7', 'F'}

    def can_move_south(self, x, y):
        if y+1 >= self.max_y:
            return False
        return self.kernel[x, y+1] in {'|', 'L', 'J'}

    def __getitem__(self, pos):
        return self.kernel[pos]

    def replace_start(self):
        x = self.start_x
        y = self.start_y
        options = set('|-JL7F')
        if self.can_move_north(x, y):
            from icecream import ic; ic('north')
            options &= {'|', 'J', 'L'}
        if self.can_move_east(x, y):
            options &= {'-', 'L', 'F'}
        if self.can_move_south(x, y):
            from icecream import ic; ic('south')
            options &= {'|', 'F', '7'}
        if self.can_move_west(x, y):
            from icecream import ic; ic('west')
            options &= {'-', '7', 'J'}
        from icecream import ic; ic(options)
        assert len(options) == 1
        self.kernel[x, y] = list(options)[0]


def load_input(filename):
    with open(filename, 'r') as file_input:
        lines = file_input.readlines()
    return Plan(lines)


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


def get_perimeter(plan):
    assert plan[plan.start_x, plan.start_y] == 'S'
    yield (plan.start_x, plan.start_y)
    steps = 0
    orientation, x, y = first_move(plan, plan.start_x, plan.start_y)
    while plan[x, y] != 'S':
        yield (x, y)
        steps += 1
        orientation, x, y = new_move(plan, orientation, x, y)


def ranglist(lst):
    lst = sorted(lst)
    if not lst:
        return []
    if len(lst) == 1:
        return [(lst[0], lst[0])]
    result = []
    while lst:
        first = lst.pop(0)
        next = first + 1
        while lst and lst[0] == next:
            next += 1
            lst.pop(0)
        result.append((first, next - 1))
    return result
