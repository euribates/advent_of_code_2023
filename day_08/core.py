
#!/usr/bin/env python3


def load_rule(line):
    name, paths = line.split(' = ')
    assert paths.startswith('(')
    assert paths.endswith(')')
    left, right = paths[1:-1].split(', ')
    return name, {'R': right, 'L': left}


def load_input(filename):
    with open(filename, 'r') as file_input:
        instructions = file_input.readline().strip()
        file_input.readline()  # Blank line
        kernel = {}
        for line in file_input:
            line = line.strip()
            name, options = load_rule(line)
            kernel[name] = options
    return instructions, kernel
