import sys
sys.stdin = open("Baekjoon/BruteForce/TwoStickers/input.txt","r")
h,w = map(int,input().split(" "))
n = int(input())
stickers = [list(map(int,input().split(" "))) for _ in range(n)]
a,b = [0,0],[0,0]
res = 0

for i in range(n-1):
    for j in range(i+1,n):
        r1 = max(stickers[i][0],stickers[i][1])
        c1 = min(stickers[i][0],stickers[i][1])
        r2 = max(stickers[j][0],stickers[j][1])
        c2 = min(stickers[j][0],stickers[j][1])
        if (r1+r2 <= h and max(c1,c2) <=w)or (c1+c2 <=w and max(r1,r2) <=h):
            res = max(res,r1*c1 + r2*c2)
        if (r1+c2 <= h and max(c1,r2) <=w) or (c1+r2 <= w and max(r1,c2) <=h):
            res = max(res,r1*c1 + r2*c2)
        if (c1+c2 <=h and max(r1,r2) <=w) or (r1+r2 <=w and max(c1,c2) <=h):
            res = max(res,r1*c1 + r2*c2)
        if (c1+r2 <=h and max(c2,r1) <=w)  or (c2+r1 <=w and max(c1,r2) <= h):
            res = max(res,r1*c1 + r2*c2)

print(res)
