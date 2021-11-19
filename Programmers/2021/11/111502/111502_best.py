from itertools import combinations

def solution(info,query):
    answer = []
    # 가능한 query 조합저장을 위한 dict
    table = {}
    for item in info:
        # dataset의 query부분과 점수 부분 분리
        conditions = item.split()[:-1]
        score = int(item.split()[-1])
        for n in range(5):
            # query 조건의 범위를 반복하며 조건에 부합하는 query 생성
            combi = list(combinations(range(4),n))
            for c in combi:
                t_c = conditions.copy()
                for v in c:
                    t_c[v] = '-'
                new_t_c = '/'.join(t_c)
                if new_t_c in table:
                    table[new_t_c].append(score)
                else:
                    table[new_t_c] = [score]
    # dataset 정렬
    for value in table.values():
        value.sort()
    #검색 부분 세분화
    for item in query:
        item = [i for i in item.split() if i != 'and']                      
        # 조건문과 점수부분 분리
        query_cnd = '/'.join(item[:-1])
        query_score = int(item[-1])
        if query_cnd in table:
            data = table[query_cnd]
            if len(data) >0:
                # 조건과 일치하는 부분의 길이를 비교하여 검색
                start, end = 0, len(data)
                while start != end and start != len(data):
                    if data[(start+end) //2] >= query_score:
                        end = (start+end) //2
                    else:
                        start = (start+end) //2 +1
                answer.append(len(data)-start)
        else :
            answer.append(0)

    return answer

if __name__ == '__main__':    
    print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

