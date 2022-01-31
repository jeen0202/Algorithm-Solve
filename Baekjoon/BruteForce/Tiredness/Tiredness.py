import sys
sys.stdin = open("Baekjoon/BruteForce/Tiredness/input.txt","r")
a,b,c,m = map(int,input().split(" "))

w = 0
if a>m:
    print(0)
    exit()
for i in range(1,25):
    works = (24-i)*b
    t = (24-i)*a - i*c
    if t<=m and works>=w:
        w=works
print(w)