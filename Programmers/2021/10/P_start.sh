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

echo "제목
-----
### 개요
### 규칙
### 매개변수 및 솔루션" > $1/README.md