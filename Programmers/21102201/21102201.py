import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(1)]

def solution(s):
    replacement = [
        ["zero","0"],
        ["one","1"],
        ["two","2"],
        ["three","3"],
        ["four","4"],
        ["five","5"],
        ["six","6"],
        ["seven","7"],
        ["eight","8"],
        ["nine","9"]
        ]
    answer = s
    for item in replacement:
        if item[0] in answer:
            answer = answer.replace(item[0],item[1])   
    return int(answer)

if __name__ == '__main__':
    print(solution(arr[0][0]))

