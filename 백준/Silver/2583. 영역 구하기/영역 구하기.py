import sys
from collections import deque

input = sys.stdin.readline

def bfs(st,si):
    q = deque()
    q.append((st,si))
    v[st][si] = 1
    cnt = 1
    while q:
        x,y = q.popleft()

        for dx,dy in (-1,0),(0,1),(1,0),(0,-1):
            nx,ny = dx+x, dy+y
            if (0<=nx<M and 0<=ny<N and v[nx][ny] == 0):
                q.append((nx,ny))
                v[nx][ny] =  1
                cnt +=1

    return cnt

M,N,K = map(int, input().split())


v = [[0] * N for _ in range(M)]

for _ in range(K):
    x1,y1,x2,y2 = map(int, input().split())

    for i in range(y1,y2):
        for j in range(x1,x2):
            v[i][j] = 1

result = []
for i in range(M):
    for j in range(N):
        if v[i][j] == 0:
            result.append(bfs(i,j))

print(len(result))
print(*sorted(result))
