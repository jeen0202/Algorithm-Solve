
import sys
import re
from itertools import chain
from collections import Counter
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(1)]

def solution(s):
    temp=[]
    answer=[]
    p = re.compile('\{[\d,?]+\}')
    for item in p.findall(s):
        item = item.strip("{}")
        temp.append(list(map(int,item.split(","))))
    temp = list(chain(*temp))
    cnt = Counter(temp)
    for item in cnt.most_common():
        answer.append(item[0])
    return answer
    


if __name__ == '__main__':    
    print(solution(arr[0][0]))

