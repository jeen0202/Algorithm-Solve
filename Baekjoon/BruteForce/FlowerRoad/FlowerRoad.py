import sys
sys.stdin = open("Baekjoon/BruteForce/FlowerRoad/input.txt","r")
from itertools import combinations
n = int(input())
p = [list(map(int,input().split(" "))) for _ in range(n)]
table = [(r,c) for r in range(n) for c in range(n)]
q = list(combinations(table,3))
dd=  [(1,0),(-1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

def check(flowers):    
    visited=[]
    total = 0
    for r,c in flowers:
        visited.append((r,c))
        total+= p[r][c]
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            dr,dc = r+dx,c+dy
            if (dr,dc) not in visited and 0<=dr<n and 0<=dc<n:
                visited.append((dr,dc))
                total+= p[dr][dc]
            else:
                return 3000
    return total
ans = 3000
for li in q:
    ans = min(ans,check(li))
print(ans)
# def check(x,y):
#     total = p[x][y]
#     for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
#         nx,ny = x+dx,y+dy
#         if nx<0 or nx>n-1 or ny <0 or ny>n-1:
#             return (False,1000)
#         else :
#             total+= p[nx][ny]
#         return (True,total)

# for i in range(n):
#     for j in range(n):
#         flag = True
#         total = p[i][j]            
#         for d in dd:                              
#             dx,dy = i+d[0],j+d[1]
#             if (dx<0 or dx>n-1) or (dy<0 or dy>n-1) or (dx,dy) in res:
#                 flag= False
#             else :
#                 if d in [(1,0),(-1,0),(0,1),(0,-1)] and flag == True:
#                     total+=p[dx][dy]
#         if flag == True:
#             for i in range(3):
#                 if total < ans[i]:
#                     ans[i] = total
#                     res[i] = (i,j)
# print(res,ans)
        

