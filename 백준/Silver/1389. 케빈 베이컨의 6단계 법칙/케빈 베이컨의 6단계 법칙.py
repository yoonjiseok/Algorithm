import sys
from collections import deque
input = sys.stdin.readline

def bfs(arr,st):
    q = deque()
    q.append(st)

    while q:
        x = q.popleft()
        for i in arr[x]:

            if (v[i] == 0):
                v[i] = v[x] + 1
                q.append(i)

    return (sum(v))

N,M = map(int , input().split())

arr = [[] for _ in range(N+1)]



for _ in range(M):
    X,Y = map(int, input().split())
    arr[X].append(Y)
    arr[Y].append(X)



ans = float('inf')
answer = 0
for i in range(N):
    v = [0] * (N + 1)
    l = (bfs(arr,i+1))
    if ans > l:
        ans = l
        answer = i+1

print(answer)