#!/bin/zsh
mkdir $1/$2
echo "import sys
sys.stdin = open(\"Baekjoon.$1/$2/input.txt\",\"r\")

" > $1/$2/$2.py

echo "제목
===
## 개요
## 규칙
## 입력 및 출력" > $1/$2/README.md

echo > $1/$2/input.txt