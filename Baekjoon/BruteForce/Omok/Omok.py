import sys
sys.stdin = open("Baekjoon/BruteForce/Omok/input.txt","r")
n= 19
dd=  [(0,1),(1,0),(1,1),(1,-1)]
p = [list(map(int,input().split(" "))) for _ in range(n)]

def check():
    for i in range(n):
        for j in range(n):
            visited = [[False for _ in range(n)] for _ in range(n)]
            if p[i][j]>0:
                visited[i][j] =1
                res = [(i,j)]

                for k in range(4):
                    cnt = 1
                    nx,ny = i+dd[k][0],j+dd[k][1]

                    while 0<=nx<19 and 0<=ny<19 and visited[nx][ny]== False and p[i][j] == p[nx][ny]:
                        cnt +=1
                        visited[nx][ny] = True
                        res.append((nx,ny))
                        nx += dd[k][0]
                        ny += dd[k][1]
                    if cnt == 5:
                        cx,cy = i-dd[k][0],j-dd[k][1]
                        if 0<=cx<19 and 0<=cy<19 and p[cx][cy]==p[i][j]:
                            continue
                        else:
                            return p[i][j], res,k
    return 0,0,0

a,b,d = check()
if a>0:
    print(a)
    if d == 1:
        print(b[0][0]+1,b[0][1]+1)
    else :
        b.sort(key = lambda x:(x[1],-x[0]))
        print(b[0][0]+1,b[0][1]+1)
else :
    print(a)