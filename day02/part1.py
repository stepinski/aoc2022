#from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    score =0

    for line in s.splitlines():
        moves=line.split()
        games=0
        if moves[1]=='X' :
            games+=1
            if moves[0]=='A':
                games+=3
            elif moves[0]=='C':
                games+=6
        elif moves[1] =='Y':
            games+=2
            if moves[0]=='A':
                games+=6
            elif moves[0]=='B':
                games+=3
        elif moves[1] =='Z':
            games+=3
            if moves[0]=='B':
                games+=6
            elif moves[0]=='C':
                games+=3
        score+=games
        
       
    return score


INPUT_S = '''\
A Y
B X
C Z
'''
EXPECTED = 15


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
