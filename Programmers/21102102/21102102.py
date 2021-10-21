import sys
import re
sys.stdin = open(sys.argv[1],"r")
arr  = [list(map(str,input().split())) for _ in range(1)]

def solution(new_id):
    #1단계    
    new_id = new_id.lower()
    #2단계    
    new_id = re.sub("[^a-z^0-9]","",new_id)
    new_id = re.sub("[^-^_^.]","",new_id)
    # #3단계
    new_id = re.sub("[.]{2,}",".",new_id)
    #new_id = re.sub("((.)\\2{1,})",".",new_id)
    #new_id = re.sub("((.)\\2{2,})",".",new_id)
    # #4단계
    new_id = re.sub("\.&|[.]$","",new_id)
    # #5단계
    # if len(new_id) ==0:
    #     new_id = 'a'
    # #6단계
    # if len(new_id) >=16:
    #     new_id = new_id[0:15]    
    # #7단계
    # while len(new_id) <=2:        
    #     new_id + new_id[-1]
    return new_id

if __name__ == "__main__":    
    print(solution(arr[0][0]))

