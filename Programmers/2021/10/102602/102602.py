import sys
import re
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(1)]

# 런타임 에러
# def solution(s):        
#     if len(s)==0 :
#         return 1
#     for i in range(len(s)):         
#         if s[i-1] == s[i]:
#             new_s = s.replace(s[i],"",2)
#             print(new_s)
#             return solution(new_s)        
#     return 0
def solution(s): 
    stack = []
    if len(s) %2 == 1:
        return 0
    if len(s) == 2 :
        return s[0] == s[1]    
    stack.append(s[0])
    
    for item in s[1:]:        
        if len(stack) > 0 and stack[-1] == item:
            stack.pop()
        else:
            stack.append(item)
    return 0 if len(stack) else 1
            


if __name__ == '__main__':    
    print(solution(arr[0][0]))

