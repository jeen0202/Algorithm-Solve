import sys
sys.stdin = open("Baekjoon/BruteForce/CoinGame/input.txt","r")
from collections import deque
dd = [(0,3,6),(1,4,7),(2,5,8),(0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6)]
def to_int(x):
    ret = 0
    for i in range(len(x)):
        ret+= x[i]*(2**i)
    return ret
def to_arr(x):
    res = bin(x)[2:]
    while len(res)<9:
        res='0'+res
    res = list(map(int,res))
    res.reverse()
    return res

def change(x):
    if x == 1: return 0
    else : return 1
def is_correct(x):
    if x == 0 or x == 511:
        return True
    return False

def game(coins):
    start = to_int(coins)
    visited = [-1 for _ in range(512)]
    visited[start] = 0
    q = deque()
    q.append(start)
    while q:
        c = q.popleft()
        if is_correct(c):
                return visited[c]
        for d in dd:
            cl = to_arr(c)
            for dc in d:
                cl[dc] = change(cl[dc])
                if visited[to_int(cl)] == -1:
                    visited[to_int(cl)] = visited[c]+1
                    q.append(to_int(cl))
    return -1



t = int(input())
for _ in range(t):
    coins = []
    v = []
    for _ in range(3):
        temp = list(input().split())
        for i in range(3):
            if temp[i] == "T": temp[i] = 1
            else : temp[i] = 0
        coins.extend(temp)
    print(game(coins))
