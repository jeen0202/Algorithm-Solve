def solution(m,n,board):
    answer=0
    rows,transBoard = "",list()
    # 원활한 제거를 위한 list 행렬 변환
    for i in range(n):
        for j in range(m-1,-1,-1):
            rows+=board[j][i]
        transBoard.append(rows)        
        rows=""
    print(transBoard)
    # 제거 위치 확인을 위한 알고리즘
    while True:
        match = []
        for i in range(n-1):
            for j in range(len(transBoard[i])-1):
                if transBoard[i][j]==transBoard[i][j+1] and transBoard[i][j:j+2]==transBoard[i+1][j:j+2]:
                    match.append((i,j))
                    #match.append((i,j+1))
                    match.append((i+1,j))
                    #match.append((i+1,j+1))
                    #print(f'{i} {j}')
        match = sorted(list(set(match)),reverse=True)
        if match == []:
            break
        for l in match:
            transBoard[l[0]]= transBoard[l[0]][:l[1]]+transBoard[l[0]][l[1]+2:]
        print(transBoard)
        
    return answer

if __name__ == '__main__':    
    #print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
    print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

