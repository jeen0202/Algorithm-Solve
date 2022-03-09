import sys
sys.stdin = open("Baekjoon/Greedy/Kindergarten/input.txt","r")
input = sys.stdin.readline
n,k = map(int,input().split())
children = list(map(int,input().split()))
cost = []
for i in range(n-1):
    cost.append(abs(children[i]-children[i+1]))
cost.sort()
print(sum(cost[:(n-k)]))