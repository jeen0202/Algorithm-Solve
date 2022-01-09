def solution(X,Y,D):
    Y -= X    
    return Y//D + (Y%D !=0)
if __name__ == '__main__':    
    print(solution(10,85,30))

