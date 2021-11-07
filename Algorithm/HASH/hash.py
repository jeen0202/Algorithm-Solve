import sys
from collections import deque
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(1)]

def hash_function(string):
    return hash(string)%8

def solution (names):
    hash_map = {}
    for name in names:       
        hash_map[hash_function(name)] = 1
    print(hash_map[hash_function('Viden')])
    return hash_map

if __name__ == '__main__':    
    print(solution(arr[0]))
