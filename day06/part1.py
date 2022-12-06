#from __future__ import annotations

import argparse
import os.path

import pytest

import support
import re

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def compute(s: str) -> int:
    counter =0
    lastfour=""
    switch=False
    stacks=[]
    procs = []
    found=0 
    for c in s:
        # print(c)
        # print(lastfour)
        # print("---")
        if c not in lastfour[-4:] :
            #if counter>3 :
            found+=1
            
        else :
            found-=1
            #counter=0

        if found ==4 and counter>=4 :
            break;

        lastfour+=c
        counter+=1
    return counter

#[['', 'D', ''], ['N', 'C', ''], ['Z', 'M', 'P'], ['', '1', '', '', '2', '', '', '3', '']]
#[['1', '2', '1'], ['3', '1', '3'], ['2', '2', '1'], ['1', '1', '2']]

INPUT_S = '''\
bvwbjplbgvbhsrlpgdmjqwftvncz:
'''
EXPECTED = 5


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
