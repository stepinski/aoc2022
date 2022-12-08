#from __future__ import annotations

import argparse
import os.path

import pytest

import support
import re

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def compute(s: str) -> int:

    current=''
    parent=''
    files= {} #{"name":"","size":0,"path":[]}
    loc=["root"]
    dirs ={"root":0}
    for line in s.splitlines():
        cmd = line.split()
        if cmd[0] == '$' :
            if cmd[1] == "cd":
                if cmd[2]== '..':
                    loc.pop()
                    current=loc[-1]
                elif cmd[2]=='/':
                    current=loc[0]
                    loc = [loc[0]]
                else :
                    loc.append(cmd[2])
                    current=cmd[2]
        
            elif cmd[1] == "ls" :
                tmp=1
            
        else :
            if cmd[0].isnumeric() :
                size=int(cmd[0])
                files[cmd[1]]=[size,loc]
                for dir in loc:
                    if dir in dirs.keys():
                        dirs[dir]+=size
                    else:
                        dirs[dir]=size

    ret={k: v for k, v in dirs.items() if v<=100000}
   # print(ret)
   # print(dirs)
    #ret2=sorted(dirs.items(), key=lambda item: item[1],reverse=True)     
    #print(ret2)
   # print(len(files.keys()))
    return sum(ret.values())

#[['', 'D', ''], ['N', 'C', ''], ['Z', 'M', 'P'], ['', '1', '', '', '2', '', '', '3', '']]
#[['1', '2', '1'], ['3', '1', '3'], ['2', '2', '1'], ['1', '1', '2']]

INPUT_S = '''\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''
EXPECTED = 95437


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
