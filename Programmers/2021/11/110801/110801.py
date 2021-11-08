import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(int,input().split())) for _ in range(2)]

def solution(priorities,location):
    hash_map = {}
    for index,item in enumerate(priorities):
        hash_map[index] = item       
    index,order = 0,1

    while True:
        print(hash_map,index,order)
        if len(hash_map) == 1:
            return order
        temp = hash_map[index]
        if temp >= max(hash_map.values()):
            if index == location:
                return order
            order+=1            
            del hash_map[index]
            print(index,temp)
        else :        
            del hash_map[index]
            hash_map[index] = temp
        index = next(iter(hash_map))
        
if __name__ == '__main__':    
    print(solution(arr[0],arr[1][0]))