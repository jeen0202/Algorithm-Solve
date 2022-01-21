import sys
sys.stdin = open("Baekjoon/Graph/Tomato2/input.txt","r")
m,n,k = map(int,input().split(" "))
print(m,n,k)
Graph = [[[0 for _ in range(m)]for _ in range(n)] for _ in range(k)]
visited=[]
for i in range(k):
    for j in range(n):
        Graph[i][j] = list(map(int,input().split(" ")))
        for l in range(m):
            if Graph[i][j][l] == 1:
                visited.append((i,j,l))
def BFS():
    return
print(visited)