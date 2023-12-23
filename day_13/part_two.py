#!/usr/bin/env python3

import core


def calc_diff(line_a, line_b):
    return sum([
        0 if char_a == char_b else 1
        for char_a, char_b in zip(line_a, line_b)
        ])


def is_cuasi_mirror(plan, candidate, height):
    backward_range = range(candidate-1, -1, -1)
    forward_range = range(candidate, height)
    return sum([
        calc_diff(plan[backguard_index], plan[forward_index])
        for backguard_index, forward_index
        in zip(backward_range, forward_range)
        ]) == 1


def find_cuasi_mirror(plan):
    height = len(plan)
    first_iter = iter(plan)
    second_iter = iter(plan)
    next(second_iter)
    for candidate, (a, b) in enumerate(zip(first_iter, second_iter), start=1):
        if is_cuasi_mirror(plan, candidate, height):
            return candidate
    return 0


def summarize(plan):
    h_mirror = find_cuasi_mirror(plan)
    v_mirror = find_cuasi_mirror(core.transpose(plan))
    return v_mirror + h_mirror * 100


def main(options):
    sol = 0
    for plan in core.load_input(options.filename):
        sol += summarize(plan)
    print(f'[Day 13] Sol. part two is: {sol}')


if __name__ == "__main__":
    options = core.get_options()
    main(options)
