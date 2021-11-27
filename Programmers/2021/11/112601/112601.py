from itertools import combinations
from collections import Counter

def solution(clothes):   
    dict = {}
    answer = 1
    val,key = list(zip(*clothes))
    for i in range(len(val)):
        if not key[i] in dict.keys():
            dict[key[i]] = val[i]            
        else:
            if type(dict.get(key[i])) != set:                
                temp = {dict.get(key[i]),val[i]}
            else :                                                
                temp = dict.get(key[i])
                temp.add(val[i])                
            dict[key[i]] = temp
    for value in dict.values():                
        if type(value) == set:            
            answer *= (len(value)+1)            
        else:
            answer *=2
    return answer-1

if __name__ == '__main__':    
    
    print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
    print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
