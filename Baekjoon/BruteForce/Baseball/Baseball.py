import sys
sys.stdin = open("Baekjoon/BruteForce/Baseball/input.txt","r")
from itertools import permutations
n = int(input())
li = list(permutations(range(1,10),3))

for _ in range(n):
    num,s,b = map(int,input().split(" "))
    num = str(num)
    rcnt = 0    
    for i in range(len(li)):
        ts,tb = 0,0
        i -= rcnt
        for j in range(3):
            cp = int(num[j])
            if cp in li[i]:
                if j == li[i].index(cp):
                    ts +=1
                else :
                    tb +=1
        if ts != s or tb !=b:
            li.remove(li[i])
            rcnt +=1
print(len(li))