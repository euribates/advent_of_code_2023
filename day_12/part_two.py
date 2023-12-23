#!/usr/bin/env python3

from core import get_options, load_input
from core import count_valid_expansions


from tqdm import tqdm


def get_total_lines(filename):
    with open(filename, 'r') as f_in:
        return len(f_in.readlines())


def main(options):
    filename = options.filename
    acc = 0
    total = get_total_lines(filename)
    from icecream import ic; ic(total)
    lines = 0
    for record, damaged_parts in tqdm(load_input(filename), total=total):
        from icecream import ic; ic(record)
        record = '{r}?{r}?{r}?{r}?{r}'.format(r=record)
        damaged_parts = damaged_parts * 5
        valid_count = count_valid_expansions(record, damaged_parts)
        from icecream import ic; ic()
        ic(record, damaged_parts, valid_count)
        acc += valid_count
        lines += 1
        if lines >= 2:
            break
    print(f'[Day 12] Sol. part two is: {acc}')


if __name__ == '__main__':
    options = get_options()
    main(options)
