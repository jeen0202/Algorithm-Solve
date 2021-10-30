import sys
from collections import Counter
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split(","))) for _ in range(1)]

def solution(str1, str2):
    str1,str2 = str1.lower(),str2.lower()
    strarr1,strarr2 = [], []    
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            strarr1.append(str1[i:i+2])
    for j in range(len(str2)-1):
        if str2[j:j+2].isalpha() :
            strarr2.append(str2[j:j+2]) 
    #combine_arr = set(strarr1).union(set(strarr2))    
    #inter_arr = set(strarr1).intersection(strarr2)
    #combine_arr = sum(Counter(strarr1),Counter(strarr2))
    count1,count2 = Counter(strarr1),Counter(strarr2)    
    #print(count1,count2)
    #print(sum(Counter(strarr1).values()))
    inter_arr = sum((count1 & count2).values())
    union_arr = sum((count1 | count2).values())
    if union_arr == 0 and inter_arr == 0:
        return 65536
    return int(inter_arr/union_arr*65536)


if __name__ == '__main__':    
    print(solution(arr[0][0],arr[0][1]))

