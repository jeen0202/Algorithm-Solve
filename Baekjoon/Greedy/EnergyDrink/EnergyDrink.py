import sys
sys.stdin = open("Baekjoon/Greedy/EnergyDrink/input.txt","r")
input = sys.stdin.readline
n = int(input())
drinks = list(map(int,input().split()))
drinks.sort(reverse=True)
ans = drinks[0]
for i in range(1,n):
    ans += drinks[i]/2
print(ans)

