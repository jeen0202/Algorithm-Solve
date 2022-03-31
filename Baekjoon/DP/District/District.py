import sys
sys.stdin = open("Baekjoon/DP/District/input.txt","r")
input = sys.stdin.readline
n,m = map(int,input().split())
grounds = []
for _ in range(n):
    grounds.append(list(map(int,input().split())))
for j in range(m):
    for i in range(1,n):
        grounds[i][j] += grounds[i-1][j]
k = int(input())
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    ans = sum(grounds[x2-1][y1-1:y2])
    if x1-2>=0:
        ans -= sum(grounds[x1-2][y1-1:y2])
    print(ans)