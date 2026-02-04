import sys
input = sys.stdin.readline
from collections import deque
N = int(input())

def bfs(st,si,cnt):
    q = deque()
    q.append((st,si))
    v[st][si] = 1
    arr[st][si] = cnt
    while q:
        x,y = q.popleft()

        for dx,dy in (-1,0),(0,-1),(1,0),(0,1):
            nx,ny = x+dx, y+dy
            if (0<=nx<N and 0<=ny<N and v[nx][ny] == 0 and arr[nx][ny] == 1):
                q.append((nx,ny))
                arr[nx][ny] = cnt
                v[nx][ny] = 1


def ans(st,si,answer):

    q = deque()
    q.append((st,si))
    v[st][si] = 1

    while q:
        x,y = q.popleft()

        if arr[x][y] != 0 and arr[x][y] != answer:
            return v[x][y] -2
        for dx,dy in (-1,0),(0,-1),(1,0),(0,1):
            nx,ny = x+dx, y+dy
            if (0<=nx<N and 0<=ny<N and v[nx][ny] == 0):
                q.append((nx,ny))
                v[nx][ny] = v[x][y]+1

arr = [list(map(int, input().split(' '))) for _ in range(N)]




result = deque()
v = [[0] * N for _ in range(N)]
cnt = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and v[i][j] == 0:
            bfs(i,j,cnt)
            cnt+=1

for i in range(N):
    for j in range(N):
        for m,n in (-1,0),(0,-1),(1,0),(0,1):
            m,n = i+m, j+n
            if 0<=m<N and 0<=n<N and arr[i][j] != 0 and arr[m][n] == 0:
                v = [[0] * N for _ in range(N)]
                result.append(ans(i,j, arr[i][j]) )


print(min(result))