def solution(m,n,board):
    for i in range(m-1):
        for j in range(n-1):
            #print(board[i][j:j+2])
            if board[i][j]==board[i][j+1] and board[i][j:j+2]==board[i+1][j:j+2]:
                print(f'{i} {j}')
                

if __name__ == '__main__':    
    print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))

