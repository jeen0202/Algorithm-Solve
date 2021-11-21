from itertools import combinations

def solution(relation):
    answer = 0
    colsize, rowsize = len(relation[0]),len(relation)
    hubos = []
    uli = []
    # 가능한 모든 조합
    for i in range(1,colsize+1):
        hubos.extend(combinations(range(colsize),i))
    for hubo in hubos:
        temp = [tuple([item[i] for i in hubo]) for item in relation]
        if len(set(temp)) == rowsize:
            uli.append(hubo)
    answer = set(uli)    
    for i in range(len(uli)):
        for j in range(i+1,len(uli)):
            if len(uli[i]) == len(set(uli[i]) & set(uli[j])):
                answer.discard(uli[j])
    return len(answer)

if __name__ == '__main__':    
    print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))

