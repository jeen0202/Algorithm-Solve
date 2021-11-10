import sys
import re
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(1)]

def solution(name):
    answer = 0
    if len(name) == name.count('A'):
        return 0
    if len(name) == 1:
        return ord(name)-65
    if name.count('A') >0:
        firstA = name.find('A')        
        for item in re.finditer(r"A+",name):
            print(item.group())
            print(item.span())
        
    else:
        answer += len(name)-1
    
    
    
    name = list(map(ord,name))
    #print(name)
    for item in name:
        answer += min([item-65,91-item])
    return answer

if __name__ == '__main__':    
    print(solution(arr[0][0]))

