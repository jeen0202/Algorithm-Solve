import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(1)]

def complete_check(s) :
    check = 0
    temp = ""
    u = ""
    v = ""
    for i in s:
        if i == "(":
            check +=1
        else :
            check -=1    
        if check <0:
            return 0   
    if check == 0:
        return 1
    else : 
        return 0
def solution(p):
    check = 0
    temp = ""
    u = ""
    v = ""
    if len(p) == 0:
        return ""       
    
    if complete_check(p):        
        return p
    else :
        for i in p:            
            if i == "(":
                check +=1
            else :
                check -=1
            temp += i
            if check == 0 :
                u = temp
                v = p[len(temp):]                               
                break;
        if complete_check(u):
            return u+solution(v)
        else :
            temp = "("+solution(v)+")"
            for i in u[1:-1]:
                if i == "(":
                    temp += ")"
                else :
                    temp += "("
            return temp
             
        

if __name__ == '__main__':    
    print(solution(arr[0][0]))

