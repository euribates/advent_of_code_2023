#!/usr/bin/env python3

import sys


def load_input(filename):
    for line in open(filename, 'r'):
        if line.strip():
            yield line.strip()


# def next_as_digit(line):
    # if len(line) == 1:
        # return line[0], ''
    # if line[0:3] == 'one':
        # return '1', line[3:]
    # if line[0:3] == 'two':
        # return '2', line[3:]
    # if line[0:5] == 'three':
        # return '3', line[5:]
    # if line[0:4] == 'four':
        # return '4', line[4:]
    # if line[0:4] == 'five':
        # return '5', line[4:]
    # if line[0:3] == 'six':
        # return '6', line[3:]
    # if line[0:5] == 'seven':
        # return '7', line[5:]
    # if line[0:5] == 'eight':
        # return '8', line[5:]
    # if line[0:4] == 'nine':
        # return '9', line[4:]
    # return line[0], line[1:]


def next_as_digit(line):
    if len(line) == 1:
        return line[0], ''
    if line[0:3] == 'one':
        return '1', line[1:]
    if line[0:3] == 'two':
        return '2', line[1:]
    if line[0:5] == 'three':
        return '3', line[1:]
    if line[0:4] == 'four':
        return '4', line[1:]
    if line[0:4] == 'five':
        return '5', line[1:]
    if line[0:3] == 'six':
        return '6', line[1:]
    if line[0:5] == 'seven':
        return '7', line[1:]
    if line[0:5] == 'eight':
        return '8', line[1:]
    if line[0:4] == 'nine':
        return '9', line[1:]
    return line[0], line[1:]


def translate(line):
    buff = []
    original = line[:]
    while line:
        char, line = next_as_digit(line)
        print(original, char, line)
        buff.append(char)
    return ''.join(buff)


# assert translate('xtwone3four') == 'x2w1ne34our'

# assert translate('two1nine') == '219'
# assert translate('abcone2threexyz') == 'abc123xyz'

# assert translate('two1nine') == '219'
# assert translate('eightwothree') == '8wo3'
# assert translate('abcone2threexyz') == 'abc123xyz'
# assert translate('xtwone3four') == 'x2ne34'
# assert translate('4nineeightseven2') == '49872'
# assert translate('zoneight234') == 'z1ight234'
# assert translate('7pqrstsixteen') == '7pqrst6teen'

# assert translate('fivepqxlpninevh2xxsnsgg63pbvdnqptmg') == '5pqxlp9vh2xxsnsgg63pbvdnqptmg'
# assert translate('eight8zlctbmsixhrvbpjb84nnmlcqkzrsix') == '88zlctbm6hrvbpjb84nnmlcqkzr6'
# assert translate('hkxqfrqmsixfplbkpkdfzzszjxmdjtdkjlprrvr3gghlrqckqtbng') == (
    # 'hkxqfrqm6fplbkpkdfzzszjxmdjtdkjlprrvr3gghlrqckqtbng'
    # )
# assert translate('zkjkctxvssix1dqb22five') == 'zkjkctxvs61dqb225'
# assert translate('4dtlmkfnm') == '4dtlmkfnm'
# assert translate('four539tkqrc') == '4539tkqrc'
# assert translate('blxqb7onetvmfjlvglrnbtdonegfourfour') == 'blxqb71tvmfjlvglrnbtd1g44'
# assert translate('lqzrclnlzrvdstgtoneseven1xrvdchn29') == 'lqzrclnlzrvdstgt171xrvdchn29'
# assert translate('tczmtfkqhthreetwo7five') == 'tczmtfkqh3275'
# assert translate('kncvqpzdtfs7') == 'kncvqpzdtfs7'

# assert translate('zclvhfz91zbdkrreightbzqttdxrone') == 'zclvhfz91zbdkrr8bzqttdxr1'

def get_two_digits_number(line):
    buff = []
    for c in line:
        if c.isdigit():
            buff.append(c)
    if not buff:
        return 0
    return int(f'{buff[0]}{buff[-1]}')


# assert translate('onetwothreefourfivesixseveneightnine') == '123456789'
# assert translate('nineeightsevensixfivefourthreetwoone') == '987654321'

assert get_two_digits_number(translate('onetwothreefourfivesixseveneightnine')) == 19
assert get_two_digits_number(translate('nineeightsevensixfivefourthreetwoone')) == 91


def sol_02(filename):
    return sum([
        get_two_digits_number(translate(line))
        for line in load_input(filename)
        ])

# assert translate('ddgjgcrssevensix37twooneightgt') == 'ddgjgcrs763721ightgt'
assert get_two_digits_number(translate('ddgjgcrssevensix37twooneightgt')) == 78


assert get_two_digits_number(translate('one')) == 11
assert get_two_digits_number(translate('two')) == 22
assert get_two_digits_number(translate('three')) == 33
assert get_two_digits_number(translate('four')) == 44
assert get_two_digits_number(translate('five')) == 55
assert get_two_digits_number(translate('six')) == 66
assert get_two_digits_number(translate('seven')) == 77
assert get_two_digits_number(translate('eight')) == 88
assert get_two_digits_number(translate('nine')) == 99

assert get_two_digits_number(translate('abcdef')) == 0

assert translate('one86') == '1ne86'
assert get_two_digits_number(translate('one86')) == 16


assert sol_02('sample') == 142


def sol_02_trace(filename):
    for line in load_input(filename):
        print(line, translate(line), get_two_digits_number(translate(line)), sep=" --> ")


def main():
    filename = sys.argv[1]
    sol_02(filename)
    print('Solution part 2:', sol_02(filename))


if __name__ == "__main__":
    main()


