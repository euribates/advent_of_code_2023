#!/usr/bin/env python3

from collections import Counter
from itertools import product
from functools import cache


SORT_ORDER = '23456789TJQKA'
SORT_MAP = {c: SORT_ORDER.index(c) for c in SORT_ORDER}


def get_strength(hand):
    return tuple([SORT_MAP[c] for c in hand])


@cache
def get_value(hand):
    count = Counter(hand)
    num_keys = len(count)
    max_count = max(count.values())
    match num_keys, max_count:
        case 5, 1:
            return 0  # High cards
        case 4, 2:
            return 1  # One pair
        case 3, 2:
            return 2  # two pair
        case 3, 3:
            return 3  # Three of a kind
        case 2, 3:
            return 4  # Full house
        case 2, 4:
            return 5  # Four of a kind
        case 1, 5:
            return 6  # Four of a kind
        case _, _:
            raise ValueError(f'La mano {hand} no es valida')


# Part two


SORT_ORDER_WITH_JOKERS = 'J23456789TQKA'
SORT_MAP_WITH_JOKERS = {
    c: SORT_ORDER_WITH_JOKERS.index(c)
    for c in SORT_ORDER_WITH_JOKERS
    }


def get_strength_with_jokers(hand):
    return tuple([SORT_MAP_WITH_JOKERS[c] for c in hand])


def expand_hand(hand, options=SORT_ORDER_WITH_JOKERS[1:]):
    assert 'J' not in options
    cards = [list(options) if c == 'J' else c for c in hand]
    for option in product(*cards):
        yield ''.join(option)


def find_best_hand(hand):
    if 'J' in hand:
        print('Joker in Hand!')
        sort_key = (get_value(hand), get_strength_with_jokers(hand))
        for candidate in expand_hand(hand):
            new_key = (get_value(candidate), get_strength_with_jokers(candidate))
            print(candidate, new_key, sort_key)
            if new_key > sort_key:
                sort_key = new_key
                hand = candidate
    return hand


@cache
def get_value_with_jokers(hand):
    hand = find_best_hand(hand)
    return get_value(hand)

