#!/usr/bin/env python3

import sys


def load_time(line):
    items = line.strip().split()
    assert items[0] == 'Time:'
    return [int(_) for _ in items[1:]]


def load_distance(line):
    items = line.strip().split()
    assert items[0] == 'Distance:'
    return [int(_) for _ in items[1:]]


def load_input(filename):
    with open(filename, 'r') as f:
        time = load_time(f.readline())
        distance = load_distance(f.readline())
    return zip(time, distance)


def find_all_times(time, distance):
    for _t in range(1, time):
        speed = _t
        distance = speed * (time - _t)
        yield distance


def main():
    filename = sys.argv[1]
    acc = 1
    for t, d in load_input(filename):
        print(f"Time {t} -> distance {d}")
        options = len([
            _d for _d 
            in find_all_times(t, d)
            if _d > d
            ])
        acc = acc * options
    print(f"Solution part one: {acc}")


if __name__ == "__main__":
    main()
