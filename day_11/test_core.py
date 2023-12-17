#!/usr/bin/env python3

import pytest

import core


def test_star():
    s0 = core.Vector2(3, 8)
    s1 = core.Vector2(5, 10)
    assert s0.distance(s1) == s1.distance(s0)
    assert s0.distance(s1) == 4


def test_star_zero():
    s0 = core.Vector2(0, 0)
    s1 = core.Vector2(0, 0)
    assert s0.distance(s1) == s1.distance(s0)
    assert s0.distance(s1) == 0


def test_star_one():
    s0 = core.Vector2(0, 0)
    assert s0.distance(core.Vector2(0, -1)) == 1
    assert s0.distance(core.Vector2(1, 0)) == 1
    assert s0.distance(core.Vector2(-1, 0)) == 1
    assert s0.distance(core.Vector2(0, 1)) == 1


def test_star_two():
    s0 = core.Vector2(0, 0)
    assert s0.distance(core.Vector2(0, -2)) == 2
    assert s0.distance(core.Vector2(-1, -1)) == 2
    assert s0.distance(core.Vector2(-1, 1)) == 2
    assert s0.distance(core.Vector2(-2, 0)) == 2
    assert s0.distance(core.Vector2(2, 0)) == 2
    assert s0.distance(core.Vector2(1, -1)) == 2
    assert s0.distance(core.Vector2(1, 1)) == 2

if __name__ == "__main__":
    pytest.main()
