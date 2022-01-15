#!/bin/bash
mkdir $1/$2
echo "import sys
sys.stdin = open(".$1/$2/input.txt","r")
def solution():
        

if __name__ == '__main__':    
    print(solution())
" > $1/$2/$2.py

echo "제목
===
## 개요
## 규칙
## 매개변수 및 솔루션" > $1/$2/README.md

echo > $1/$2/input.txt