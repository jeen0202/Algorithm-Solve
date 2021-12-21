#!/bin/zsh
mkdir $1
echo "def solution():
        

if __name__ == '__main__':    
    print(solution())
" > $1/$1.py

echo "제목
-----
### 개요
### 규칙
### 매개변수 및 솔루션" > $1/README.md