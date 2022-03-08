import sys
sys.stdin = open("Baekjoon/Greedy/Octopus/input.txt","r")
input = sys.stdin.readline
n = int(input())
hands = []
hands.append("1")
for _ in range(n-1):
    if hands[-1] == "1":
        hands.append("2")
    else: 
        hands.append("1")
if n%2 == 1:
    hands[-1] = "3"
ans = " ".join(hands)
print(ans)