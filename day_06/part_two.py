#!/usr/bin/env python3

import sys


from tqdm import tqdm


def load_time(line):
    items = line.strip().split()
    assert items[0] == 'Time:'
    return int(''.join([_ for _ in items[1:]]))


def load_distance(line):
    items = line.strip().split()
    assert items[0] == 'Distance:'
    return int(''.join([_ for _ in items[1:]]))


def load_input(filename):
    with open(filename, 'r') as f:
        time = load_time(f.readline())
        distance = load_distance(f.readline())
    return time, distance


def count_victories(time, distance):
    acc = 0
    for _t in tqdm(range(1, time)):
        speed = _t
        _d = speed * (time - _t)
        if _d > distance:
            acc += 1
    return acc


assert load_input('sample') == (71530, 940200)


def main():
    filename = sys.argv[1]
    time, distance = load_input(filename)
    print(f"Time: {time}")
    print(f"Distance: {distance}")
    sol = count_victories(time, distance)
    print(f"Sol. part two: {sol}")


if __name__ == "__main__":
    main()
