import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(2)]

def solution(numbers,hand):
    answer = ""
    now = {"lAxis":[3,0],"rAxis":[3,2]}
    length = {"left":[-1,-1],"right":[-1,-1]}
    axis = [-1,-1]     
    for item in numbers:
        if item == 0:
            axis = [3,1]
        else :
            axis= [(item-1)//3,(item+2)%3] 
        length['left']= [abs(now['lAxis'][0]-axis[0]),abs(now['lAxis'][1]-axis[1])]
        length['right']=[abs(now['rAxis'][0]-axis[0]),abs(now['rAxis'][1]-axis[1])]
        l_length = abs(now['lAxis'][0]-axis[0])+abs(now['lAxis'][1]-axis[1])
        r_length = abs(now['rAxis'][0]-axis[0])+abs(now['rAxis'][1]-axis[1])
        if item in (1,4,7):
            answer+= "L"
            now['lAxis'] = axis
        elif item in (3,6,9):
            answer += "R"
            now['rAxis'] = axis
        else:
            if l_length == r_length :                               
                if hand == "left":
                    answer += "L"
                    now['lAxis'] = axis
                else :
                    answer += "R"
                    now['rAxis'] = axis
            elif l_length < r_length:
                answer+= "L"
                now['lAxis'] = axis
            else:
                answer += "R"
                now['rAxis'] = axis
        print(item, axis, now, length)        
    return answer

if __name__ == '__main__':    
    print(solution(list(map(int,arr[0])),arr[1][0]))

