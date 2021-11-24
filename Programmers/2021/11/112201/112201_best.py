import sys
sys.stdin = open(sys.argv[1],'r')
arr  = input()

def solution(s) :    
    code = {"[":"]","{":"}","(":")"}
    if len(s) == 0 or len(s)%2 != 0:
        return 0
    answer =  0
    for index in range(len(s)):                   
        temp = list(s[index:]+s[:index])
        stack = [] 
               
        while temp:
            e = temp.pop(0)
            if e in ["[","{","("]:
                stack.append(e)
            elif len(stack) == 0:
                break
            else :
                if stack[-1] in ["]","}",")"]:
                    break                
                elif code[stack[-1]] == e:
                    stack.pop()
                else: 
                    stack.append(e)
        if len(stack)== 0 and len(temp)==0:
            answer +=1
    return answer

if __name__ == '__main__':    
    print(solution(arr))
