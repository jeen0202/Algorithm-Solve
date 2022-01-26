import sys
sys.stdin = open("Baekjoon/Graph/ChooseNumber/input.txt","r")
from collections import defaultdict,deque
n = int(input())
p = defaultdict(int)
for i in range(1,n+1):
    p[i] = int(input())
maximum = len(p)
q = deque()

ans = set()
for k,v in p.items():
    visited = []
    if k == v:
        ans.add(k)
        continue
    q.append(k)
    while q:
        k = q.popleft()
        if visited and p[k] == visited[0]:
            ans.update(visited)
            break
        if p[k] not in visited:
            visited.append(p[k])
            q.append(p[k])
ans = sorted(list(ans))
print(len(ans))
for e in ans:
    print(e)