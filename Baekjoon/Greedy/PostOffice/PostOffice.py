import sys
sys.stdin = open("Baekjoon/Greedy/PostOffice/input.txt","r")
input = sys.stdin.readline
n = int(input())
towns = []
for i in range(n):
    towns.append(list(map(int,input().split())))
towns.sort(key = lambda x : x[0])
midv = round(sum(p for _, p in towns)/2) 
count = 0
for i,p in towns:
    count += p
    if count >= midv:
        print(i)
        break
# ans = [0]*n
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             continue
#         ans[i]+= abs(towns[i][0]-towns[j][0])*towns[j][1]
# print(ans.index(min(ans))+1)