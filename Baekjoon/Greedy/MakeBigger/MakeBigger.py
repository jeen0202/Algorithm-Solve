import sys
sys.stdin = open("Baekjoon/Greedy/MakeBigger/input.txt","r")
input = sys.stdin.readline
n,k = map(int,input().split())
number = list(input())
ans = []
cnt = k
for i in range(n):
    while cnt >0 and ans and ans[-1] < number[i]:
        ans.pop()
        cnt -=1
    ans.append(number[i])
print("".join(ans[:n-k]))