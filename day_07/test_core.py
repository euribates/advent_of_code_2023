#!/usr/bin/env python3

import pytest

from core import get_value
from core import get_strength_with_jokers


def test_get_value_high_cards():
    assert get_value('A3K87') == 0  # high cards


def test_get_value_one_pair():
    assert get_value('A3A87') == 1  # one_pair


def test_get_value_two_pair():
    assert get_value('A3A37') == 2  # two pair


def test_get_value_three_of_a_kind():
    assert get_value('A3337') == 3  # three of a kind


def test_get_value_full_house():
    assert get_value('A333A') == 4  # Full house


def test_get_value_four_of_a_kind():
    assert get_value('A3333') == 5  # Four of a kind


def test_get_value_five_of_a_kind():
    assert get_value('AAAAA') == 6  # Five of a kind


def test_get_strength_with_jokers():
    assert get_strength_with_jokers('J2345') == (0, 1, 2, 3, 4)
    assert get_strength_with_jokers('234AJ') == (1, 2, 3, 12, 0)


from core import expand_hand


def test_expand_hand():
    assert list(expand_hand('JA2A2', ['A', '2'])) == [
        'AA2A2',
        '2A2A2',
        ]

def test_expand_hand_two_jokers():
    assert list(expand_hand('234JJ', ['2', '3', '4'])) == list([
        '23422',
        '23423',
        '23424',
        '23432',
        '23433',
        '23434',
        '23442',
        '23443',
        '23444',
        ])


from core import find_best_hand


def test_find_best_hand():
    assert find_best_hand('32T3K') == '32T3K'
    assert find_best_hand('KK677') == 'KK677'
    assert find_best_hand('T55J5') == 'T5555'
    assert find_best_hand('KTJJT') == 'KTTTT'
    assert find_best_hand('QQQJA') == 'QQQQA'


if __name__ == "__main__":
    pytest.main()
