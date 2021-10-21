#!/bin/bash
mkdir $1
echo "import sys
sys.stdin = open(sys.argv[1],"r")
arr  = [list(map(int,input().split())) for _ in range(2)]

def solution():
        

if __name__ == "__main__":    
    print(solution())
" > $1/$1.py