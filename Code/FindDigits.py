#!/usr/bin/env python3

import sys
import os


def find_digits(path):
    if os.path.exists(path):
        digits = []
        with open(path) as fobj:
            for line in fobj:
                for c in line:
                    if c.isdigit():
                        digits.append(c)
        return ''.join(digits)
    else:
        return 'file not found!'


if __name__ == '__main__':
    if len(sys.argv) > 1:
        digits = find_digits(sys.argv[1])
        print(digits)
    else:
        print('Wrong parameter')
