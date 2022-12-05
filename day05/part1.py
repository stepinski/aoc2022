#from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    counter =0
    switch=False
    stacks=[]
    procs = []
    for line in s.splitlines():
        if line :
            r=line.replace('[', '')
            r=r.replace(']', '') 
            r=r.replace('move ', '')
            r=r.replace('from ', '')
            r=r.replace('to ', '')   
            r = r.split() 
            
            if switch ==False :
                stacks.append(r) 
            else:
                procs.append(r)
        else :
            switch=True
    
    return stacks


INPUT_S = '''\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''
EXPECTED = 2


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
