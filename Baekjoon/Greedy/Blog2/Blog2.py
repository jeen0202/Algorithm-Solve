import sys
sys.stdin = open("Baekjoon/Greedy/Blog2/input.txt","r")
n = int(input())
p = input()
count = [0,0]

for i in range(n-1):
    if p[i] == p[i+1]:
        if i ==n -2:
            if p[i+1] == 'B':
                count[0] +=1
            else:
                count[1] +=1
    else:
        if p[i] == 'B':
            count[0] +=1
        else :
            count[1] +=1
        if i == n-2:
            if p[i+1] == 'B':
                count[0] +=1
            else:
                count[1] +=1
print(min(count)+1)