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
    elves=[]
    elve =0
    maxcalories=0
    for line in s.splitlines():
        if line :
            elve += int(line)
        else:
            elves.append(elve)
            #   if elve>maxcalories:
            #    maxcalories=elve
            elve=0
    
    elves.sort(reverse=True)
    total=sum(elves[0:3])
    return total


INPUT_S = '''\
5
5
5

1
1
1
1

3

22

21

'''
EXPECTED = 58


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
