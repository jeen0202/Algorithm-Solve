import sys
sys.stdin = open("Baekjoon/BruteForce/FourSquares/input.txt","r")
import math
n = int(input())
def check(x):
    if math.sqrt(x).is_integer() : return 1
    for i in range(1,int(math.sqrt(x))+1):
        if math.sqrt(int(x-math.pow(i,2))).is_integer() : return 2
    for i in range(1,int(math.sqrt(x))+1):
        for j in range(1,int(math.sqrt(int(x-math.pow(i,2))))+1):
            if math.sqrt(x-math.pow(i,2)-math.pow(j,2)).is_integer () : return 3
    return 4

print(check(n))