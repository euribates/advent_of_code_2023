#!/usr/bin/env python3

import pytest

import core


def test_find_groups():
    assert core.find_groups('#.#.###') == (1, 1, 3)
    assert core.find_groups('.#...#....###.') == (1, 1, 3)
    assert core.find_groups('.#.###.#.######') == (1, 3, 1, 6)
    assert core.find_groups('####.#...#...') == (4, 1, 1)
    assert core.find_groups('#....######..#####.') == (1, 6, 5)
    assert core.find_groups('.###.##....#') == (3, 2, 1)


def test_count_valid_expansions():
    assert core.count_valid_expansions('???.###', (1, 1, 3)) == 1
    assert core.count_valid_expansions('.??..??...?##.', (1, 1, 3)) == 4
    assert core.count_valid_expansions('?#?#?#?#?#?#?#?', (1, 3, 1, 6)) == 1
    assert core.count_valid_expansions('????.#...#...', (4, 1, 1)) == 1
    assert core.count_valid_expansions('????.######..#####.', (1, 6, 5)) == 4
    assert core.count_valid_expansions('?###????????', (3, 2, 1)) == 10


if __name__ == "__main__":
    pytest.main()
