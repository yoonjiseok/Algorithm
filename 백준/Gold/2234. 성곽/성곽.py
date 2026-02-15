import sys
input = sys.stdin.readline
from collections import deque

def bfs(st,si,r_n):
    q = deque()
    q.append((st,si))
    v[st][si] = r_n

    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    cnt = 1
    while q:
        x,y = q.popleft()

        for i in range(4):
            if (arr[x][y] & (1 << i)) == 0:
                nx = x+dx[i]
                ny = y+dy[i]

                if 0 <= nx < M and 0 <= ny < N and v[nx][ny] == 0:
                    v[nx][ny] = r_n
                    q.append((nx, ny))
                    cnt+=1

    return cnt


N,M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]


cnt = 1

v = [[0]*N for _ in range(M)]

answer1 = 0
room_size = []

for i in range(M):
    for j in range(N):
        if(v[i][j] == 0):
            width = bfs(i,j,cnt)
            cnt+=1
            room_size.append(width)
            if answer1 < width:
                answer1 = width


answer2 = []
max_room_size = 0
for i in range(M):
    for j in range(N):
        for dx,dy in (-1,0),(0,-1),(1,0),(0,1):
            nx,ny = i+dx,j+dy
            if 0<=nx<M and 0<=ny<N and v[nx][ny] != v[i][j]:
                if max_room_size < (room_size[int(v[nx][ny]) -1] + room_size[int(v[i][j]) - 1]):
                    max_room_size = (room_size[int(v[nx][ny]) -1] + room_size[int(v[i][j]) - 1])


print(cnt-1)
print(answer1)
print(max_room_size)