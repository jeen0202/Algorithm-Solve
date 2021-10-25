from os import TMP_MAX
import sys
import re
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(1)]

def solution(s):
    answer = 1000
    for n in range(1, len(s)//2+1):
        res =''
        cnt = 1
        temp=s[:n]
        for i in range(n,len(s)+n,n):
            if temp == s[i:i+n]:
                cnt+=1
            else:
                if cnt ==1:
                    res+=temp
                else:
                    res+=str(cnt)+temp
                temp=s[i:i+n]
                cnt=1
        answer = min(answer,len(res))
        print(res)
    return answer

if __name__ == '__main__':    
    print(solution(str(arr[0][0])))