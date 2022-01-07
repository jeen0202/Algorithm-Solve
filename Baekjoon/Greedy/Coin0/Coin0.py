import sys
sys.stdin = open("Baekjoon/Greedy/Coin0/input.txt","r")


def solution():
    N,K = map(int,input().split())
    A = []
    coins = 0
    for _ in range(N):
        A.append(int(input()))
    A.reverse()
    for coin in A:
        if coin >K :
            continue
        coins += K//coin
        K = K%coin
        if K == 0:
            print(coins)

if __name__ == "__main__":
    solution()