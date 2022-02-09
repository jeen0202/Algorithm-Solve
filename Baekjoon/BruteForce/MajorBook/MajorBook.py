import sys
sys.stdin = open("Baekjoon/BruteForce/MajorBook/input.txt","r")
t = list(input())
n = int(input())
p = []
for _ in range(n):
    a,b = map(str,input().split(" "))
    p.append((b,int(a)))

def matching(word,book,price):
    cnt = 0
    for alpha in word:
        if alpha in book:
            cnt +=1
            book = book.replace(alpha," ",1)
            if cnt == len(word):
                return price
    return 100000*n

result = []
for i in range(1 << n):
    search = ""
    total = 0
    for j in range(n):
        if (i & 1 << j) != 0:
            search += p[j][0]
            total += p[j][1]
    result.append(matching(t,search,total))
result = min(result)
if result == 100000*n:
    result = -1
print(result)