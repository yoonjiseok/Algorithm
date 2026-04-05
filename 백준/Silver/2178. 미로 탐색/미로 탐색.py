import sys
from collections import deque
input = sys.stdin.readline

def bfs(st,si, et,ei):
    q = deque()
    q.append((st,si))
    v[st][si] = 1
    while q:
        x,y = q.popleft()

        if x == et and y == ei:
            return v[x][y]

        for dx,dy in (-1,0),(0,1),(0,-1),(1,0):
            nx,ny = x+dx, y+dy

            if (0<=nx<=et and 0<=ny<=ei and arr[nx][ny] == 1 and v[nx][ny] == 0):
                q.append((nx,ny))
                v[nx][ny] = v[x][y] + 1



N,M = map(int,input().split(' '))
v = [[0]*M for _ in range(N)]
arr = [list(map(int, input().strip())) for _ in range(N)]

print(bfs(0,0,N-1,M-1))