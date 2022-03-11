import sys
sys.stdin = open("Baekjoon/Greedy/Habor/input.txt","r")
input = sys.stdin.readline
n = int(input())
crains = list(map(int,input().split()))
crains.sort(reverse=True)
m = int(input())
boxes = list(map(int,input().split()))
boxes.sort(reverse=True)
moved = [0]*m
if max(crains) < max(boxes):
    print(-1)
    exit()
ans = 0
while sum(moved)!=m:
    for i in range(n):
        for j in range(m):
            if moved[j]==0 and crains[i] >= boxes[j]:
                 moved[j] = 1
                 break
    ans +=1
print(ans)