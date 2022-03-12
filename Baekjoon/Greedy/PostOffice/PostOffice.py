import sys
sys.stdin = open("Baekjoon/Greedy/PostOffice/input.txt","r")
input = sys.stdin.readline
n = int(input())
towns = []
for i in range(n):
    towns.append(list(map(int,input().split())))
towns.sort(key = lambda x : x[0])
ans = [0]*n
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        ans[i]+= abs(towns[i][0]-towns[j][0])*towns[j][1]
print(ans.index(min(ans))+1)