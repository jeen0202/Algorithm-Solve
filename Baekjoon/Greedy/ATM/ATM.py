import sys
sys.stdin = open("Baekjoon/Greedy/ATM/input.txt","r")


def solution():
    N = int(input())
    time = 0
    p = list(map(int,input().split()))
    p.sort()
    for i in range(N):
        time += p[i]*(N-i)
    print(time)

if __name__ == "__main__":
    solution()