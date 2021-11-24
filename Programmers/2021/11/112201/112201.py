import sys
sys.stdin = open(sys.argv[1],'r')
arr  = input()

code = {"]":"[","}":"{",")":"("}

def solution(s):
    if len(s) == 0 or len(s)%2 != 0:
        return 0
    keys = list(code.keys())
    answer=  0
        
    for index in range(len(s)):            
        temp = list(s[index:]+s[:index])        
        top = len(temp)-1
        #print(temp,top)                              
        while top>=0:
            x = temp.pop(top)
            top-=1
            print(x,list(temp))            
            if x not in keys or code[x] not in temp:
                print('con1')
                break
            y = code[x]
            # 2차 조건 
            for i in range(top,0,-1):
                if temp[i] == y:
                    start = i
                    break            
                print('con2')
                break               
            else:
                temp.remove(code[x])
                top-=1                
                if len(temp) %2 != 0 :
                    break;
            if len(temp) == 0:
                answer +=1            
    return answer

if __name__ == '__main__':    
    print(solution(arr))

