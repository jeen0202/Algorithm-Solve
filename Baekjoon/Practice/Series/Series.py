import sys
sys.stdin = open("Baekjoon/Practice/Series/input.txt","r")
sys.setrecursionlimit(10**6)

def solution():
    N = int(input())
    p = [] 
    for _ in range(N):
        p.append(float(input())) 
    for i in range(1,N):
        p[i] = max(p[i],p[i]*p[i-1])         
    print(f'{max(p):.3f}')
if __name__ == "__main__":
    solution()