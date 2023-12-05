#!/usr/bin/env python3

import sys
from core import load_input



def find_location(seed, all_maps):
    for i, rules in enumerate(all_maps):
        for rule in rules:
            if rule.in_range(seed):
                seed = rule.translate(seed)
                break
    return seed


def main():
    filename = sys.argv[1]
    seeds, all_maps = load_input(filename)
    locations = [find_location(seed, all_maps) for seed in seeds]
    sol = min(locations)
    print(f"Sol. part one: {sol}")


if __name__ == "__main__":
    main()
