import sys
sys.stdin = open("Baekjoon/Graph/Illumination/input.txt","r")
from collections import deque

# dy에 맞춰 짝홀 구분
dy = [0,1,1,0,-1,-1]
dx = [[1,0,-1,-1,-1,0],[1,1,0,-1,0,1]]
W,H = map(int,input().split(" "))
# 외부를 파악하기 위해 그리드 크기 확대
Graph = [[0 for _ in range(W+2)] for _ in range(H+2)]
for i in range(1,H+1):
    Graph[i][1:W+1] = (list(map(int,input().split(" "))))

def BFS(y,x):
    queue = deque()
    queue.append((y,x))
    visited = [[False for _ in range(W+2)]for _ in range(H+2)]
    visited[y][x] = True
    cnt =0
    while queue:
        y,x = queue.popleft()

        for i in range(6):
            ny = y +dy[i]
            nx = x +dx[y%2][i]
            if 0<= ny < H+2 and 0 <= nx < W+2:
                if Graph[ny][nx] == 0 and not visited[ny][nx]:
                    queue.append((ny,nx))
                    visited[ny][nx] = True
                elif Graph[ny][nx] == 1:
                    cnt +=1
    return cnt
print(BFS(0,0))