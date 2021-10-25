import sys
import re
sys.stdin = open(sys.argv[1],"r")
arr  = [list(map(str,input().split())) for _ in range(1)]

def solution(new_id):
    check = ""
    #1단계    
    new_id = new_id.lower()
    #2단계
    # st = re.sub('[^a-z0-9\-_.]', '', st)
    for item in new_id :
        if item.isalnum() or item in '-_.' :
            check += item  
    #3단계
    # st = re.sub('\.+', '.', st)    
    while '..' in check:
        check = check.replace('..','.')
    #4단계
    # st = re.sub('^[.]|[.]$', '', st)
    if check.endswith('.'):
        check = check[:-1]
    if check.startswith('.'):
        check = check[1:]
    #5단계
    if len(check) ==0:
        check = 'a'
    #6단계
    # st = 'a' if len(st) == 0 else st[:15]
    # st = re.sub('^[.]|[.]$', '', st)
    if len(check) >=16:
        check = check[0:15]
    if check.endswith('.'):
        check = check[:-1]    
    #7단계
   # st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    while len(check) <3:        
        check += check[-1]
    return check

if __name__ == "__main__":    
    print(solution(arr[0][0]))

# 정규식 방식





 