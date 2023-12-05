#!/usr/bin/env python3

import dataclasses


@dataclasses.dataclass(order=True)
class Rule:
    start: int
    stop: int
    offset: int

    def __init__(self, line):
        numbers = [int(n) for n in line.split()]
        assert len(numbers) == 3
        destination_range_start = int(numbers[0])
        source_range_start = int(numbers[1])
        range_length = int(numbers[2])
        self.start = source_range_start
        self.stop = source_range_start + range_length
        self.offset = destination_range_start - source_range_start

    def in_range(self, number):
        return self.start <= number < self.stop

    def translate(self, number):
        if self.in_range(number):
            return number + self.offset
        return number


def load_seeds(source):
    line = source.readline()
    _ = source.readline() # Ignore empty line
    _seeds, numbers = line.split(': ')
    return [int(n) for n in numbers.split()]


def load_map(name, source):
    _name = source.readline()
    assert _name.startswith(name)
    result = []
    line = source.readline().strip()
    while line:
        result.append(Rule(line))
        line = source.readline().strip()
    return sorted(result)


def load_input(filename):
    with open(filename, 'r') as source:
        seeds = load_seeds(source)
        all_maps = [
            load_map('seed-to-soil', source),
            load_map('soil-to-fertilizer', source),
            load_map('fertilizer-to-water', source),
            load_map('water-to-light', source),
            load_map('light-to-temperature', source),
            load_map('temperature-to-humidity', source),
            load_map('humidity-to-location', source),
            ]
    return seeds, all_maps

# Part two

def expand_ranges(seeds):
    while seeds:
        value = seeds.pop(0)
        length = seeds.pop(0)
        for _ in range(length):
            yield value
            value += 1



