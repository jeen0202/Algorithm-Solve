import sys
sys.stdin = open("Baekjoon/DP/SeriesSum/input.txt","r")

def solution():
    answer = [-1001]
    N = int(input())
    p = list(map(int,input().split()))
    answer.append(p[0])    
    for i in range(1,N+1):
        answer.append(max())
    

if __name__ == "__main__" :
    solution()