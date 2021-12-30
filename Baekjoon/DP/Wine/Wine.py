import sys
sys.stdin = open("Baekjoon/DP/Wine/input.txt","r")

def solution():
    N = int(input())
    w = []
    for _ in range(N):
        w.append(int(input()))
    answer = sum(w)
    for i in range(0,N-5,6):
        answer-=(min(w[i]+w[i+3],w[i+1]+w[i+4],w[i+2]+w[i+5]))   
    print(answer)

if __name__ == "__main__":
    solution()