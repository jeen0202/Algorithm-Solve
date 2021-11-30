
def solution(brown,yellow):    
    for i in range(1,yellow+1):
        if i * i > yellow:
            break
        if yellow % i:
            continue
        x = yellow//i
        if 2*(i+x+2) == brown:
            return[x+2,i+2] 
if __name__ == '__main__':    
    print(solution(10,2))
    print(solution(8,1))
    print(solution(24,24))

