from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    n = 0
    #for c in support.parse_numbers_split(s):
     #   print(c)
    elve =0
    maxcalories=0
    for line in s.splitlines():
        if line :
            elve += int(line)
        else:
            if elve>maxcalories:
                maxcalories=elve
            elve=0
    
        # if c == '(':
        #     n += 1
        # elif c == ')':
        #     n -= 1
        # else:
        #     raise AssertionError(f'unexpected: {c!r}')
    return maxcalories


INPUT_S = '''\
3
3
4

0

2
'''
EXPECTED = 10


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
