import sys
sys.stdin = open("Baekjoon/Greedy/MakeBigger/input.txt","r")
input = sys.stdin.readline
n,k = map(int,input().split())
number = list(input())
for i in range(k):
    for j in range(1,n):
        if number[j] > number[j-1]:
            del number[j-1]
            break
print(int("".join(number)))
