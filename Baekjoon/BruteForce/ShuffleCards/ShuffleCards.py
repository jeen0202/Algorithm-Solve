import sys
sys.stdin = open("Baekjoon/BruteForce/ShuffleCards/input.txt","r")
n = int(input())
graph = [[[]for _ in range(n)]for _ in range(n)]
finalCards = list(map(int,input().split()))

def rotate(l,n):
    return l[n:] + l[:n]
def findK(k,cards):    
    cards = rotate(cards,-2**k)
    check = 2**k
    for i in range(2,k+2):
        cards[:check] = rotate(cards[:check],-2**(k-i+1))
        check = 2**(k-i+1)              
    return cards        

for i in range(1,n+1):
    for j in range(1,n+1):
        if 2**i <n and 2**j < n:   
            if finalCards == findK(j,findK(i,list(range(1,n+1)))):
                print(i,j)