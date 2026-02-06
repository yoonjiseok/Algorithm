import sys
from collections import deque

def bfs(st,si,et,ei,K_cnt):
    if st==et and si == ei:
        print(1)
        return 1
    q = deque()
    q.append((st,si,K_cnt))
    v[K_cnt][st][si] = 1
    while q:
        x,y,k_cnt = q.popleft()

        for dx,dy in (-1,0),(0,1),(0,-1),(1,0):
            nx,ny = dx+x,dy+y

            if (nx == et and ny == ei):
                print(v[k_cnt][x][y]+1)
                return 1

            if (0<=nx<=et and 0<=ny<=ei and arr[nx][ny] == 1):
                if (v[k_cnt-1][nx][ny]==0 and k_cnt > 0):
                    q.append((nx,ny,k_cnt-1))
                    v[k_cnt-1][nx][ny] = v[k_cnt][x][y] + 1

            elif (0<=nx<=et and 0<=ny<=ei and arr[nx][ny] == 0):
                if (v[k_cnt][nx][ny]==0):
                    q.append((nx,ny,k_cnt))
                    v[k_cnt][nx][ny] = v[k_cnt][x][y] + 1

    print(-1)
    return 0
input = sys.stdin.readline

N,M = map(int, input().split())


arr = [list(map(int, input().strip())) for _ in range(N)]

v = [[[0]*M for _ in range(N)] for _ in range(2)]


bfs(0,0,N-1,M-1,1)
