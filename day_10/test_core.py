#!/usr/bin/env python3

import pytest

from core import Plan
from core import ranglist


def test_move_north():
    plan = Plan([
        '-7|',
        '|SJ',
        'L--',
        ])
    assert plan.can_move_north(1, 1) is True
    assert plan.can_move_north(0, 1) is False
    assert plan.can_move_north(2, 1) is True
    assert plan.can_move_north(2, 2) is False


def test_move_south():
    plan = Plan([
        '-7|',
        '|SJ',
        'L--',
        ])
    assert plan.can_move_south(1, 1) is False
    assert plan.can_move_south(0, 1) is True
    assert plan.can_move_south(2, 1) is False
    assert plan.can_move_south(2, 2) is False


def test_move_west():
    plan = Plan([
        '-7|',
        '|SJ',
        'L--',
        ])
    assert plan.can_move_west(0, 0) is False 
    assert plan.can_move_west(1, 0) is True
    assert plan.can_move_west(2, 0) is False

    assert plan.can_move_west(0, 1) is False
    assert plan.can_move_west(1, 1) is False
    assert plan.can_move_west(2, 1) is False

    assert plan.can_move_west(0, 2) is False
    assert plan.can_move_west(1, 2) is True
    assert plan.can_move_west(2, 2) is True
    

def test_move_east():
    plan = Plan([
        '-7|',
        '|SJ',
        'L--',
        ])
    assert plan.can_move_east(0, 0) is True
    assert plan.can_move_east(1, 0) is False
    assert plan.can_move_east(2, 0) is False

    assert plan.can_move_east(0, 1) is False
    assert plan.can_move_east(1, 1) is True
    assert plan.can_move_east(2, 1) is False

    assert plan.can_move_east(0, 2) is True
    assert plan.can_move_east(1, 2) is True
    assert plan.can_move_east(2, 2) is False


def test_ranglist_empty_list():
    assert list(ranglist([])) == []


def test_ranglist_one_item():
    assert list(ranglist([2])) == [(2, 2)]


def test_ranglist_two_items():
    assert list(ranglist([2, 3])) == [(2, 3)]
    assert list(ranglist([0, 1])) == [(0, 1)]


def test_ranglist_three_items():
    assert list(ranglist([1, 2, 3])) == [(1, 3)]


def test_ranglist_one_gap():
    assert list(ranglist([0, 1, 3, 4, 5])) == [(0, 1), (3, 5)]


def test_ranglist_one_gap_one_last_item():
    assert list(ranglist([0, 1, 3, 4, 5, 7])) == [(0, 1), (3, 5), (7, 7)]


def test_ranglist_five_items():
    assert list(ranglist([0, 1, 2, 3, 4])) == [(0, 4)]



if __name__ == "__main__":
    pytest.main()
