from itertools import combinations
from collections import Counter

def solution(clothes):   
    dict = {}
    comb = []
   
    val,key = list(zip(*clothes))
    for i in range(len(val)):
        if not key[i] in dict.keys():
            dict[key[i]] = val[i]            
        else:
            temp = {dict.get(key[i]),val[i]}
            dict[key[i]] = temp
    for i in range(len(dict)+1):
        comb.extend(combinations(dict.values(),i))
    return comb

if __name__ == '__main__':    
    print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))

