
def solution(bridge_length,weight,truck_weights):
    answer = 0
    bri = [0 for _ in range(bridge_length)]    
    while len(truck_weights)>0:
        bri.pop(0)
        if sum(bri)+truck_weights[0]<=weight:
            bri.append(truck_weights.pop(0))
        else: 
            bri.append(0)        
        answer+=1
        if len(truck_weights) == 0:
            answer += len(bri)
    return answer

if __name__ == '__main__':    
    print(solution(2,10,[7,4,5,6]))
    print(solution(100,100,[10]))

