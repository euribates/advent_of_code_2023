#!/usr/bin/env python3

from core import get_options, load_input


def main(options):
    data = load_input(options.filename)
    sol = len(list(data))

    print(f'[Day {{ num}}] Sol. part one is: {sol}')


if __name__ == '__main__':
    options = get_options()
    main(options)
