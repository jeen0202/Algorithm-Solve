import sys
sys.stdin = open("Baekjoon/Graph/MovingMaze/input.txt","r")
graph = [list(map(list,input().split()))for _ in range(8)]
print(graph)

