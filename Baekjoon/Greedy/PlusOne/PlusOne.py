
import sys
sys.stdin = open("Baekjoon/Greedy/PlusOne/input.txt","r")
input = sys.stdin.readline
n = int(input())
products = [int(input())for _ in range(n)]
products.sort(reverse=True)
ans = 0
for i in range(n):
    if i %3 == 2:
        continue
    ans+=products[i]        
print(ans)