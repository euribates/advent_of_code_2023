#!/usr/bin/env python3

import sys
import functools

from tqdm import tqdm

from core import load_input
from core import expand_ranges


def how_many_seeds(seeds):
    return sum(seeds[::-2])


assert how_many_seeds([79, 14, 55, 13]) == 27


def main():
    filename = sys.argv[1]
    seeds, all_maps = load_input(filename)

    def find_location(seed):
        for rules in all_maps:
            for rule in rules:
                if rule.stop < seed:
                    continue
                if rule.in_range(seed):
                    seed = rule.translate(seed)
                    break
                if seed < rule.start:
                    break
        return seed

    total_num_of_seeds = how_many_seeds(seeds)
    min_location = float("inf")
    for seed in tqdm(expand_ranges(seeds), total=total_num_of_seeds):
        location = find_location(seed)
        if location < min_location:
            min_location = location
    print(f"Sol. part one: {min_location}")


if __name__ == "__main__":
    main()
