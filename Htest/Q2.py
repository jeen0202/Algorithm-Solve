import sys
sys.stdin = open('./Htest/input02.txt','r')
from collections import defaultdict
def solution():
    N = int(input())
    dict = defaultdict(int)
    for i in range(N):
        dict[i+1]
    p = []
    for _ in range(int(N*(N-1)/2)):
        p.append(list(map(int,input().split(" "))))
    for order in p:
        if order[2] == 1:
            dict[order[0]] +=1
        else: dict[order[1]]+=1
    sorted_dict = sorted(dict.items(),key = lambda x: x[1],reverse=True)
    answer = ""
    for item in sorted_dict:
        answer += f"{item[0]} "
    return answer

if __name__ == "__main__":
    print(solution())