# import sys
# sys.stdin = open(sys.argv[1],'r')
# arr  = [list(map(자료형,input().split())) for _ in range(argv개수)]

def solution(info,query):
    answer = []
    info_table = []
    score_table = []
    query_table = []
    for item in info:
        info_table.append(item.split()[:-1])
        score_table.append(item.split()[-1])
    print(info_table)    
    for item in query:
        item = item.replace('and',"")                       
        query_table.append(item.split())   
    for query in query_table:
        temp = []
        for i in range(len(query)):
            print(query[i])
            if i ==4:
                count = 0
                for score in score_table:                    
                    if int(query[i])<=int(score):                        
                        count +=1
                temp.append(count)
            elif query[i] == '-':
                temp.append(len(info_table))                
            else:                
                temp.append(info_table.count(str(query[i])))        
        print(temp)
        answer.append(min(temp))
    return answer

if __name__ == '__main__':    
    print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

