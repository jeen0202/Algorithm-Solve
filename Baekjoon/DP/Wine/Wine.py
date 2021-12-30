import sys
sys.stdin = open("Baekjoon/DP/Wine/input.txt","r")

def solution():
    N = int(input())
    w,answer = [0],[0]
    for _ in range(N):
        w.append(int(input()))
    answer.append(w[1])
    if N>1:
        answer.append(w[1]+w[2])
    for i in range(3,N+1):
        answer.append(max(answer[i-1],answer[i-2]+w[i],answer[i-3]+w[i-1]+w[i]))   
    print(answer[N])

if __name__ == "__main__":
    solution()