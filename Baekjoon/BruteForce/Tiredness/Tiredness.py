import sys
sys.stdin = open("Baekjoon/BruteForce/Tiredness/input.txt","r")
a,b,c,m = map(int,input().split(" "))
dd = [(a,b),(0,-c)]
h = 0
t = 0
ans = 0
if a>m:
    print(0)
    exit()
for _ in range(24):
    if t + a <= m:
        ans += b
        t+=a
    else:
        if t-c <0:
            t = 0
        else :
            t -=c
print(ans)
