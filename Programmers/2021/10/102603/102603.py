import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(int,input().split())) for _ in range(2)]
temp = []
for item in list(input().split()) :    
    li = (item.split(','))
    temp.append(list(map(int,li)))

def solution(rows,columns,queries):
    return rows,columns,queries
    

if __name__ == '__main__':    
    print(solution(arr[0][0],arr[1][0],temp))

