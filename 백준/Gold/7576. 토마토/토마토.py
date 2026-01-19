from collections import deque
import sys

def bfs(adj,st):
    q = deque()
    cnt = 0
    for i in st:
        sx,sy = i
        v[sx][sy] = 1
        q.append((i))

    while q:
        x,y = q.popleft()

        for dx,dy in (-1,0), (1,0), (0,1),(0,-1):
            nx,ny = x+dx, y+dy

            if(0<=nx<N and 0<=ny<M and v[nx][ny] == 0 and adj[nx][ny] == -1):
                v[nx][ny] = -1
            if (0<=nx<N and 0<=ny<M and v[nx][ny] == 0 and adj[nx][ny] != -1):
                v[nx][ny] = v[x][y] + 1
                q.append((nx,ny))
                cnt += 1

    return cnt

input = sys.stdin.readline

M,N = map(int,(input().split()))

arr = [list(map(int,input().split())) for _ in range(N)]

v = [[0] * M for _ in range(N)]
M_cnt =0
m_v = 0

st = []
for i in range(N):
    for j in range(M):
        if (arr[i][j] == 1):
            st.append((i,j))
        if (arr[i][j] == -1):
            M_cnt += 1

x_size = len(st)

cntt = bfs(arr , st)


for i in range(N):
    for j in range(M):
        if m_v < v[i][j]:
            m_v = v[i][j]

if ((M*N) - x_size - M_cnt != cntt):
    print(-1)
else:
    print(m_v-1)
