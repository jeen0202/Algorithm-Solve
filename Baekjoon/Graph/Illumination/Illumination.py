import sys
sys.stdin = open("Baekjoon/Graph/Illumination/input.txt","r")
from collections import deque
# 짝수 
dex = [-1,-1,0,0,1,1]
dey = [0,1,-1,1,0,1]
# 홀수
dox = [-1,-1,0,0,1,1]
doy = [-1,0,-1,1,-1,0]
W,H = map(int,input().split(" "))
Graph = []
queue = deque()
outline = set()
ans = 0
for i in range(H):
    Graph.append(list(map(int,input().split(" "))))
    for j in range(W):
        if Graph[i][j] == 0:
            queue.append([i,j])
            
def DFS(Graph=Graph,queue=queue):
    ans = 0
    while queue:
        x,y = queue.popleft()
        w,cnt = 0,0        
        for i in range(6):
            if x%2==1:
                nx = x+dox[i]
                ny = y+doy[i]
            else:
                nx = x+dex[i]
                ny = y+dey[i]
            if 0<=nx<H and 0<=ny<W:
                if Graph[nx][ny]==1:
                    cnt+=1
                    w+=1
                    if ny in [0,W-1] :
                        outline.add((nx,ny))
                    if nx in [0,H-1]:
                        outline.add((nx,ny))
        if cnt != 6:
            ans += w
    return(ans)
ans = DFS()
for x,y in outline:
    if x in [0,H-1]:
        ans +=2
        if x%2 == 0 and y==W-1:
            ans +=2
        if x%2 == 1 and y==0:
            ans +=2
    elif y in [0,W-1]:
        ans+=1
        if x%2 == 0 and y==W-1:
            ans +=2
        if x%2 == 1 and y==0:
            ans +=2
print(ans)
        
        
