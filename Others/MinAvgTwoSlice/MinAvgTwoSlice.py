from itertools import combinations

def solution(A):
    p = []
    for item in combinations(range(len(A)),2):
        if item[1]-item[0] >1:
            ss = A[item[0]:item[1]]       
            p.append([item[0],sum(ss)/len(ss)])
    index = 0
    mini = p[0][1]
    for avg in p:
        if mini>avg[1]:
            index = avg[0]
            mini = avg[1]
    return index

if __name__ == '__main__':    
    print(solution([4,2,2,5,1,5,8]))

