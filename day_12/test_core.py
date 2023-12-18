#!/usr/bin/env python3

import pytest

import core


def test_get_options():
    print('test_get_options')
    for opt in core.get_options():
        print(opt)



if __name__ == "__main__":
    pytest.main()
