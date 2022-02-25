import sys
sys.stdin = open("Baekjoon/Greedy/LostBracket/input.txt","r")
n = list(input())
flag = False

for i in range(len(n)):
    if not flag and n[i] == '-':
        n.insert(i+1,'(')
        flag = not flag
    if flag and n[i+1] == '-':
        n.insert(i+1,')')
    # if n[i] in ["-","+"]:
    #     if not flag and n[i] == '-':
    #         n.insert(i+1,'(')
    #     else:
    #         n.insert(i+1,')')
    #     flag = not flag

if flag:
    n.append(")")
print(n)
print(eval("".join(n)))

