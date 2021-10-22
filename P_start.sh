#!/bin/bash
mkdir $1
echo "import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(자료형,input().split())) for _ in range(argv개수)]

def solution():
        

if __name__ == '__main__':    
    print(solution())
" > $1/$1.py

touch $1/input.txt