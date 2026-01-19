import sys
from collections import deque

def dfs(si,sj,ei,ej,k):

    q = deque()
    q.append((0,0,k))
    v[0][0][k] = 1

    while q:
        x, y, k_cnt = q.popleft()

        if x == ei and y == ej:
            print(v[x][y][k_cnt] - 1)
            return 1


        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0:
                if v[nx][ny][k_cnt] == 0:
                    v[nx][ny][k_cnt] = v[x][y][k_cnt] + 1
                    q.append((nx, ny, k_cnt))


        if k_cnt > 0:
            for dx, dy in [(-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0:
                    if v[nx][ny][k_cnt - 1] == 0:
                        v[nx][ny][k_cnt - 1] = v[x][y][k_cnt] + 1
                        q.append((nx, ny, k_cnt - 1))


input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(H)]

v = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]



e = dfs(0,0,H-1,W-1,K)

if (e != 1):
    print(-1)


