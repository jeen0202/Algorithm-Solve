from itertools import combinations

def solution(info,query):
    answer = []
    table = {}
    for item in info:
        conditions = item.split()[:-1]
        score = int(item.split()[-1])
        for n in range(5):
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

    for value in table.values():
        value.sort()

    for item in query:
        item = [i for i in item.split() if i != 'and']                      
        query_cnd = '/'.join(item[:-1])
        query_score = int(item[-1])
        if query_cnd in table:
            data = table[query_cnd]
            if len(data) >0:
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

