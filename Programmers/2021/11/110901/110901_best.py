import sys
from itertools import permutations
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(1)]

def solution(numbers):
    a = set()
    for i in range(len(numbers)):
        a |= set(map(int, map("".join, permutations(list(numbers), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)


if __name__ == '__main__':    
    print(solution(arr[0][0]))

