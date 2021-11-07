import sys
import re
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(1)]

def solution(phone_book):
    phone_book = sorted(phone_book)
    for phone_number1, phone_number2 in zip(phone_book,phone_book[1:]):
        print(phone_number1,phone_number2)
        if phone_number2.startswith(phone_number1):
            return False        
    return True

if __name__ == '__main__':    
    print(solution(arr[0]))
