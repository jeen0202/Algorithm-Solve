import sys
sys.stdin = open('./Htest/input01.txt','r')
def solution():
    answer = 0
    N = int(input())
    P = list(map(int,input().split()))
    C = list(map(int,input().split()))
    for i,m in enumerate(C):
        left = min(P[i],C[i])
        right = min(C[i]-left,P[i+1])
        P[i+1] -= right
        answer += left+right
    return answer

if __name__ == "__main__":
    print(solution())