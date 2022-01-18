import sys
sys.stdin = open("Baekjoon/Graph/HouseComplex/input.txt","r")

from collections import deque
N = int(input())
Graph,ans = [],[]
for _ in range(N):
    Graph.append(list(map(int,list(input()))))
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS(start,Graph=Graph):
    queue = deque()
    cnt = 1
    queue.append(start)
    Graph[start[0]][start[1]] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx< 0 or ny<0 or nx>=N or ny >=N:
                continue
            if Graph[nx][ny] ==0:
                continue
            if queue.count([nx,ny]):
                continue
            cnt +=1
            Graph[nx][ny] = 0
            queue.append([nx,ny])    
    ans.append(cnt) 

for i in range(N):
    for j in range(N):
        if Graph[i][j] == 1:
            BFS([i,j])
ans.sort()
print(len(ans))
for a in ans:
    print(a)