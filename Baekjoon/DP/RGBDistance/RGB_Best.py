import sys
sys.stdin = open("Baekjoon/DP/RGBDistance/input.txt","r")

def solution() :
    N = int(input())
    p = []
    for i in range(N):
        p.append(list(map(int,input().split())))
    for i in range(1,len(p)):
        p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
        p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
        p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
    #print(p)
    print(min(p[N - 1][0], p[N - 1][1], p[N - 1][2]))

if __name__ == "__main__":
    solution()