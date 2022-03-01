import sys
sys.stdin = open("Baekjoon/Greedy/GasStation/input.txt","r")
n = int(input())
road = list(map(int,input().split()))
cost = list(map(int,input().split()))
mincost = cost[0]
ans = mincost*road[0]
for i in range(1,n-1):
    mincost = min(mincost,cost[i])
    ans += mincost*road[i]
print(ans)
    
