import sys
from collections import deque 
input = sys.stdin.readline

def bfs(c):

    q = deque([c]) 

    v[c] = 1

    while q:
        x = q.popleft() 

        for i in arr[x]:
            if (v[i] == 0):
                v[i] = 1 
                q.append(i)

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

v = [0] * (N+1)

cnt = 0

for i in range(1, N + 1): 
    if(v[i] == 0):
        bfs(i)
        cnt += 1 


print(cnt)