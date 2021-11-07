import sys
import re
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(1)]

def solution(phone_book):
    ansewr = True
    hash_map = {}
    
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
    

if __name__ == '__main__':    
    print(solution(arr[0]))
