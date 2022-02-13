import sys
sys.stdin = open("Baekjoon/BruteForce/AnB2/input.txt","r")
s = list(input())
t = list(input())
flag = 0
def check(t):
    global flag
    if len(t) == len(s):
        if t == s:               
            print(1)
            exit()
        return
    if t[0] == 'B':
        t = t[::-1]
        t.pop()
        check(t)
        t.append("B")
        t = t[::-1]

    if t[-1] == 'A':
        t.pop()
        check(t)
        t.append("A")

check(t)
print(0)

    

