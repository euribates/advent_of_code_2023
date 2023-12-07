#!/usr/bin/env python3

import sys

from core import get_value_with_jokers, get_strength_with_jokers

SORT_ORDER = 'J23456789TQKA'
SORT_MAP = {c: SORT_ORDER.index(c) for c in SORT_ORDER}


def get_strength(hand):
    return tuple([SORT_MAP[c] for c in hand])


def load_input(filename):
    for line in open(filename, 'r'):
        hand, bid = line.strip().split()
        yield (hand, int(bid))


def main():
    filename = sys.argv[1]
    hands = []
    for hand, bid in load_input(filename):
        value = get_value_with_jokers(hand),
        strength = get_strength_with_jokers(hand)
        hands.append((value, strength, hand, bid))
    hands.sort()
    acc = 0
    for rank, (value, strength, hand, bid) in enumerate(hands, start=1):
        print(rank, strength, hand, bid)
        acc += rank * bid
    print(f"Solution part two: {acc}")


if __name__ == "__main__":
    main()
