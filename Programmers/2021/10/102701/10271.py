import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(int,input().split())) for _ in range(2)]
temp = []
for item in list(input().split()) :    
    li = (item.split(','))
    temp.append(list(map(int,li)))

def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i])

def solution(rows,columns,queries):
    # row, colums에 맞는 이차원 list 생성
    arr= []
    answer = []
    for i in range(rows):
        arr.append(list(range(columns*i+1,columns+(columns*i)+1)))
    # 회전 시작
    for item in queries:        
        temp =  arr[item[0]-1][item[1]-1]
        min = temp    
        for j in range(item[0]-1,item[2]-1):
            if min > arr[j+1][item[1]-1]:
                min = arr[j+1][item[1]-1]             
            arr[j][item[1]-1] = arr[j+1][item[1]-1]
            
        for j in range(item[1]-1,item[3]-1):
            if min > arr[item[2]-1][j+1]:
                min = arr[item[2]-1][j+1]         
            arr[item[2]-1][j] = arr[item[2]-1][j+1]
        
        for j in range(item[2]-1,item[0]-1,-1):  
            if min > arr[j-1][item[3]-1]:
                min = arr[j-1][item[3]-1]      
            arr[j][item[3]-1] = arr[j-1][item[3]-1]
        
        for j in range(item[3]-1,item[1],-1):
            if min >  arr[item[0]-1][j-1]:
                min =  arr[item[0]-1][j-1] 
            arr[item[0]-1][j] = arr[item[0]-1][j-1] 
        arr[item[0]-1][item[1]] = temp
        
        answer.append(min)
    return answer
    

if __name__ == '__main__':    
    print(solution(arr[0][0],arr[1][0],temp))

