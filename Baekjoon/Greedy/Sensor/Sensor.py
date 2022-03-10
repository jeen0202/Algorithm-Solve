import sys
sys.stdin = open("Baekjoon/Greedy/Sensor/input.txt","r")
input = sys.stdin.readline
n = int(input())
k = int(input())
sensors = list(map(int,input().split()))
sensors.sort()
distance = []
for i in range(n-1):
    distance.append((sensors[i+1]-sensors[i]))
distance.sort()
print(distance)
print(sum(distance[:(n-k)]))