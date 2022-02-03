import sys
sys.stdin = open("Baekjoon/BruteForce/Biggest/input.txt","r")
from itertools import product
n,k = map(int,input().split(" "))
p = list(map(str,input().split(" ")))
length = len(str(n))
for i in range(length,0,-1):
    temp = list(product(p,repeat=i))
    answer = -1

    for j in temp:
        if int("".join(j)) <= n:
            answer = max(answer,int("".join(j)))
    if answer >=0:
        print(answer)
        exit()
#tlist =["".join(e) for e in ]
#print(tlist)
# p = list(map(str,input().split(" ")))
# nlist = list(map(str,str(n)))
# ans = ""
# p.sort(reverse=True)
# cnt = 0
# temp = ""
# for line in nlist:
#     for c in p:
#         if int(ans+c)-int(temp+nlist[cnt])<=0:
#             ans += c
#             temp += nlist[cnt]
#             cnt +=1
#             break        
#print(int(ans))