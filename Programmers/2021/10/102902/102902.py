import sys
import re
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split(","))) for _ in range(1)]

def solution(str1,str2):
    str1,str2 = str1.lower(),str2.strip().lower()
    strarr1,strarr2 = [], []    
    for i in range(len(str1)-1):
        if re.compile('[a-z]\S').match(str1[i:i+2]):
            strarr1.append(str1[i:i+2])
    for j in range(len(str2)-1):
        if re.compile('[a-z]\S').match(str2[j:j+2]) :
            strarr2.append(str2[j:j+2]) 
    combine_arr = set(strarr1+strarr2)    
    inter_arr = list(set(strarr1).intersection(strarr2))
    print(combine_arr,inter_arr)
    if len(inter_arr) == 0 and len(combine_arr) == 0:
        return 65536
    return int(len(inter_arr)/len(combine_arr)*65536)


if __name__ == '__main__':    
    print(solution(arr[0][0],arr[0][1]))

