#!/usr/bin/env python3

import pytest

from core import Rule
from core import expand_ranges


def test_rule_50_98_2():
    rule = Rule('50 98 2')
    assert rule.start == 98
    assert rule.stop == 100
    assert rule.offset == -48


def test_rule_50_98_2_check():
    rule = Rule('50 98 2')
    assert rule.in_range(97) is False
    assert rule.in_range(98) is True
    assert rule.in_range(99) is True
    assert rule.in_range(100) is False


def test_rule_50_98_2_translate():
    rule = Rule('50 98 2')
    assert rule.translate(97) == 97
    assert rule.translate(98) == 50
    assert rule.translate(99) == 51
    assert rule.translate(100) == 100


def test_rule_52_50_48():
    rule = Rule('52 50 48')
    assert rule.start == 50
    assert rule.stop == 98
    assert rule.offset == 2


def test_expand_ranges_50_13():
    assert list(expand_ranges([10, 3])) == [10, 11, 12]


def test_expand_ranges_79_14_55_13():
    assert list(expand_ranges([79, 14, 55, 13])) == [
        79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92,
        55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
        ]


if __name__ == "__main__":
    pytest.main()
