import sys
sys.stdin = open("Baekjoon/Greedy/getHoney/input.txt","r")
n = int(input())
honeys = list(map(int,input().split()))
prefix_sum = []
prefix_sum.append(honeys[0])
for i in range(1,n):
    prefix_sum.append(prefix_sum[i-1]+honeys[i])
ans = 0
for i in range(1,n):
    prefix_sum.append(prefix_sum[i-1] + honeys[i])
for i in range(1,n-1):
    ans = max(ans,prefix_sum[n-2] + prefix_sum[i-1]-honeys[i])
for i in range(1,n-1):
    ans = max(ans,prefix_sum[n-1] - honeys[0] + prefix_sum[n-1]-prefix_sum[i]-honeys[i])
for i in range(1,n-1):
    ans = max(ans,prefix_sum[n-2]-honeys[0] + honeys[i])
print(ans)
#ans.append(sum(honeys[:n-1],honeys[n+1:]))


#print(max(ans))
