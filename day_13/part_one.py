#!/usr/bin/env python3

import core


def is_mirror(plan, candidate, height):
    backward_range = range(candidate-1, -1, -1)
    forward_range = range(candidate, height)
    return all([
        plan[backguard_index] == plan[forward_index]
        for backguard_index, forward_index
        in zip(backward_range, forward_range)
        ])


def find_mirror(plan):
    height = len(plan)
    first_iter = iter(plan)
    second_iter = iter(plan)
    next(second_iter)
    for candidate, (a, b) in enumerate(zip(first_iter, second_iter), start=1):
        if a == b:  # Candidate found
            if is_mirror(plan, candidate, height):
                return candidate
    return 0


def summarize(plan):
    h_mirror = find_mirror(plan)
    v_mirror = find_mirror(core.transpose(plan))
    return v_mirror + h_mirror * 100


def main(options):
    sol = 0
    for plan in core.load_input(options.filename):
        sol += summarize(plan)
    print(f'[Day 13] Sol. part one is: {sol}')


if __name__ == '__main__':
    options = core.get_options()
    main(options)
