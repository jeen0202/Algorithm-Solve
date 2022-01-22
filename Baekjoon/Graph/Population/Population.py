import sys
sys.stdin = open("Baekjoon/Graph/Population/input.txt","r")
from collections import deque
dd = [(-1,0),(1,0),(0,-1),(0,1)]
n,l,r = map(int,input().split(" "))
Graph = []
for i in range(n):
    Graph.append(list(map(int,input().split(" "))))

# def DFS():
#     ans = 0 
#     visited = [[0 for _ in range(n)]for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if visited[i][j] == 0:
#                 stack = [(i,j)]
#                 nChange = set()
#                 while stack:
#                     x,y = stack.pop()
#                     if visited[x][y] == 0:
#                         visited[x][y] = 1
#                         for k in range(4):
#                             nx,ny = x+dd[k][0], y+dd[k][1]
#                             if 0<= nx <n and 0<= ny < n:
#                                 if l<= abs(Graph[x][y]-Graph[nx][ny]) <=r :
#                                     stack.append(((nx,ny)))
#                                     nChange.add((nx,ny))
#                 if len(nChange) >0:
#                     output = round(sum(Graph[i[0]][i[1]] for i in nChange)/len(nChange))
#                     for (ix,iy) in nChange:
#                         Graph[ix][iy] = output
#                     ans = max(ans,len(nChange))
#     return ans
def BFS():
    visited = [[False for _ in range(n)]for _ in range(n)]
    ans = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False :
                visited[i][j] = True
                change = []
                queue = deque()
                queue.append((i,j))
                change.append((i,j))
                while queue:
                    x,y = queue.popleft()
                    for k in range(4):
                        nx,ny = (sum(elem) for elem in zip(dd[k],(x,y)))
                        if 0<= nx <n and 0<= ny < n and not visited[nx][ny]:
                                if l<= abs(Graph[x][y]-Graph[nx][ny]) <=r :
                                    change.append((nx,ny))
                                    queue.append((nx,ny))
                                    visited[nx][ny] = True
                if len(change)>1 :
                    ans = True
                    group = sum(Graph[cx][cy]for cx,cy in change)// len(change)
                    for ncx,ncy in change:
                        Graph[ncx][ncy] = group
    return ans


day = 0
while True:
    flag = BFS()
    if not flag:
        break
    day+=1
print(day)