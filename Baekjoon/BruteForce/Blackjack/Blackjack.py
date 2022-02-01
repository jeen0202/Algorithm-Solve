import sys
sys.stdin = open("Baekjoon/BruteForce/Blackjack/input.txt","r")
from itertools import combinations
n,m = map(int,input().split(" "))
cards = list(map(int,input().split(" ")))
combi = list(combinations(cards,3))
ans = 0
for c in combi:
    if sum(c) <=m:
        ans = max(ans,sum(c))
print(ans)
# cards.sort(reverse=True)
# print(cards)
# ans = []
# for card in cards:
#     if card + sum(ans) <= m and len(ans)<3:
#         ans.append(card)

# print(sum(ans))
