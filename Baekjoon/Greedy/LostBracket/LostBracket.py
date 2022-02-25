import sys
sys.stdin = open("Baekjoon/Greedy/LostBracket/input.txt","r")
n = list(input().split('-'))
box = []
for i in n:
    plus = 0
    s = i.split('+')
    for j in s:
        plus += int(j)
    box.append(plus)
ans = box[0]
for k in range(1,len(box)):
    ans -= box[k]
print(ans)

