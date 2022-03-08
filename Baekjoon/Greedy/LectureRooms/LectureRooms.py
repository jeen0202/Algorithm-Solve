from operator import le
import sys
sys.stdin = open("Baekjoon/Greedy/LectureRooms/input.txt","r")
import heapq
input = sys.stdin.readline
n = int(input())
lectures = [list(map(int,input().split())) for _ in range(n)]
lectures.sort(key=lambda x:x[0])
q = []
for lecture in lectures:
    if q and q[0] <= lecture[0]:
        heapq.heappop(q)
    heapq.heappush(q,lecture[1])

print(len(q))
    

