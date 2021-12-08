def solution(m,n,board):
    rows,transBoard = "",list()
    
    for i in range(n):
        for j in range(m-1,-1,-1):
            rows+=board[j][i]
        transBoard.append(rows)        
        rows=""
    print(transBoard)
    match = []
    for i in range(n-1):
        for j in range(m-1):
            if transBoard[i][j]==transBoard[i][j+1] and transBoard[i][j:j+2]==transBoard[i+1][j:j+2]:
                match.append((i,j))
                match.append((i,j+1))
                match.append((i+1,j))
                match.append((i+1,j+1))
                #print(f'{i} {j}')
    match_clean = sorted(list(set(match)))
    print(match_clean)
                

if __name__ == '__main__':    
    print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))

