import sys
sys.stdin = open("Baekjoon/BruteForce/DNA/input.txt","r")
n,m = map(int,input().split(" "))
dnas= [str(input()) for _ in range(n)]
hammings = [0 for _ in range(n)]
d = {'A':0,'C':1,'G':2,'T':3}
dd = {0:'A',1:'C',2:'G',3:'T'}
dnas.sort()
ans= ['',0]
for j in range(m):
    cnts = [0 for _ in range(4)]
    for i in range(n):
        cnts[d.get(dnas[i][j])]+=1
        temp = max(cnts)
        tempi = cnts.index(temp)
    ans[0]+=(dd.get(tempi))
    ans[1]+= n-temp

for line in ans:
    print(line)