import sys
sys.stdin = open("Baekjoon/DP/IntTriangle/input.txt","r")

def solution():
    N = int(input())
    p = []
    for _ in range(N):
        p.append(list(map(int,input().split())))
    for i in range(1,N):
        for j in range(i+1):            
            if j == 0 :
                p[i][j] = p[i][j]+p[i-1][j]
            elif j == i:
                p[i][j] = p[i][j]+p[i-1][j-1]
            else :
                p[i][j] = p[i][j] + max(p[i-1][j],p[j-1][j-1])                
    print(p)
if __name__ == "__main__":
    solution()