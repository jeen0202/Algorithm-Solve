import sys
sys.stdin = open("Baekjoon/BruteForce/Cards/input.txt","r")
from itertools import permutations
n = int(input())
k = int(input())
p = [str(input()) for _ in range(n)]
temp = list("".join(e) for e in permutations(p,k))
print(len(set(temp)))