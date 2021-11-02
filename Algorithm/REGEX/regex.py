import sys
import re
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(1)]
arr = " ".join(arr[0])

def solution(s):    
    p = re.compile("[a-z]+")    
    print(f'match : {p.match(s)}')
    print(f'search : {p.search(s)}')
    print(f'findall : {p.findall(s)}')
    m = p.search(s)
    print(m.group(),m.start(),m.end(),m.span())
    p = re.compile("^python\s\w+",re.MULTILINE)
    
    data= """python one
life is too short
python two
you need python
python three"""
    print(p.findall(data))
    

if __name__ == '__main__':    
    solution(arr)