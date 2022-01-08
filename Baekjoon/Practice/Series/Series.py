import sys
sys.stdin = open("Baekjoon/Practice/Series/input.txt","r")
sys.setrecursionlimit(10**6)

def solution():
    N = int(input())
    p = [] 
    for _ in range(N):
        p.append(float(input()))        
    dp = p.copy()      
    for i in range(len(p)):        
        for j in range(i+1,len(p)):                  
            dp[i] = max(dp[i],eval('*'.join(map(str,p[i:j]))))            
    print(f'{max(dp):.3f}')
if __name__ == "__main__":
    solution()