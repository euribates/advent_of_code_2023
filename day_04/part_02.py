#!/usr/bin/env python3

import sys
from collections import defaultdict


def load_input(filename):
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    for line in open(filename, 'r'):
        card, numbers = line.split(': ')
        _, card_num = card.split()
        winners_numbers, owned_numbers = numbers.split(' | ')
        yield (
            int(card_num),
            [int(_) for _ in winners_numbers.split()],
            [int(_) for _ in owned_numbers.split()],
            )


def main():
    filename = sys.argv[1]
    owned_cards = defaultdict(int)
    for card, winners_numbers, owned_numbers in load_input(filename):
        owned_cards[card] += 1
        matches = len(set(winners_numbers) & set(owned_numbers))
        for _ in range(owned_cards[card]):
            for index in range(matches):
                owned_cards[card + index + 1] += 1
    sol = sum(owned_cards.values())
    print(f'Sol. part two: {sol}')


if __name__ == "__main__":
    main()
