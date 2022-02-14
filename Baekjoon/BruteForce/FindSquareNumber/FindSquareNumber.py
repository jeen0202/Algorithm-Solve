import sys
import math
sys.stdin = open("Baekjoon/BruteForce/FindSquareNumber/input.txt","r")
n,m = map(int,input().split())
p = [list(map(int,input())) for _ in range(n)]
ans = -1

for i in range(n):
    for j in range(m):
        for di in range(-n,n):
            for dj in range(-m,m):
                if di == 0 and dj == 0 :
                    continue
                x = i
                y = j
                s = ""
                st = 0
                while 0<=x <n and 0<=y <m:
                    s += str(p[x][y])
                    st +=1
                    val = int("".join(s))
                    val = math.sqrt(val)
                    if val == int(val):
                        ans = max(ans, math.pow(int(val),2))
                    
                    x = i+di*st
                    y = j+dj*st
print(int(ans))
