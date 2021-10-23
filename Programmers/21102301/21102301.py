import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split(","))) for _ in range(1)]

def solution(record):
    answer = []
    u_list = {}
    for item in record:
        command,uid = item.split()[0], item.split()[1]
        if command == "Enter" or command == "Change":
            u_list.update({uid:item.split()[2]})          
    for item in record:
        command,uid = item.split()[0], item.split()[1]
        if command == "Enter":
            nick = u_list.get(uid)
            answer.append(nick+"님이 들어왔습니다.")           
        elif command == "Leave":
            nick = u_list.get(uid)
            answer.append(nick+"님이 나갔습니다.")
            u_list.pop('uid',uid)
                
    #print(u_list)        
    return answer

if __name__ == '__main__':    
    print(solution(arr[0]))

