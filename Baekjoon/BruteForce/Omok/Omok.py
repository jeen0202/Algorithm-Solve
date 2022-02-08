import sys
sys.stdin = open("Baekjoon/BruteForce/Omok/input.txt","r")
from collections import deque
n,m = 19,19
dd=  [(0,1),(1,0),(1,1)]
p = [list(map(int,input().split(" "))) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
count = [[-1,-1,0],[-1,-1,0]]
for line in p:
    print(line)

def count_1(start):
    sx,sy = start
    q = deque()
    q.append((sx,sy))
    visited[sx][sy] = 1
    while q:
        x,y = q.popleft()
        for dx,dy in dd:
            nx,ny = x+dx,y+dy
            if visited[nx][ny] == 0 and p[nx][ny] == 1:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))
                    if visited[nx][ny] == 5:
                        print(1)
                        print(sx,sy)
def count_2(start):
    sx,sy = start
    q = deque()
    q.append((sx,sy))
    visited[sx][sy] = 1
    while q:
        x,y = q.popleft()
        for dx,dy in dd:
            nx,ny = x+dx,y+dy
            if visited[nx][ny] == 0 and p[nx][ny] == 2:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))
                    if visited[nx][ny] == 5:
                        print(2)
                        print(sx,sy)
for i in range(19):
    for j in range(19):
        if p[i][j] == 1:
            count_1((i,j))
        elif p[i][j] == 2:
            count_2((i,j))