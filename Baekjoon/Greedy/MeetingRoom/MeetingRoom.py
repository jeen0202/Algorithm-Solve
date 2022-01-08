from os import name
import sys
sys.stdin = open("Baekjoon/Greedy/MeetingRoom/input.txt","r")

def solution():
    N = int(input())
    p,answer= [],[]
    for _ in range(N):
        p.append(list(map(int,input().split())))
    p.sort(key=lambda x:x[1])
    for meet in p:
        if len(answer) ==0:
            answer.append(meet)
            continue
        if meet[0] >= answer[-1][1]:
            answer.append(meet)
        # flag = True
        # for ans in answer :
        #     if max(ans[0],meet[0])<min(ans[1],meet[1]):
        #         flag=False
        # if flag == True:
        #     answer.append(meet)    
    print(len(answer))
if __name__ == "__main__":
    solution()