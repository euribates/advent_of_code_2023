#!/usr/bin/env python3

from core import get_options, load_input
from core import expand

def main(options):
    data = load_input(options.filename)
    sol = len(list(data))

    for sol in expand('???.###', (1,1,3)):
        print(sol)
    print(f'[Day 12] Sol. part one is: {sol}')


if __name__ == '__main__':
    options = get_options()
    main(options)
