dict = {'A':1,'C':2,'G':3,'T':4}
def solution(S,P,Q):
    N = len(P)    
    answer = []
    M = list(map(lambda x:(P[x],Q[x]),range(N)))
    for ss in M:
        sss = S[ss[0]:ss[1]+1]
        for key in dict.keys():        
            if key in sss: 
                answer.append(dict[key])
                break
    return(answer)
if __name__ == '__main__':    
    print(solution("CAGCCTA",[2,5,0],[4,5,6]))

