import sys
input = sys.stdin.readline
from collections import deque

def bfs(S_index, W_index, D_index):

    go_q = deque()
    wa_q = deque()
    d_x,d_y = D_index.popleft()
    go_q.append(S_index.pop())

    for _ in range(len(W_index)):
        wa_q.append(W_index.popleft())

    while go_q:

        for _ in range(len(wa_q)):
            wa_x, wa_y = wa_q.popleft()
            for wa_dx, wa_dy in (-1,0),(1,0),(0,1),(0,-1):
                wa_nx, wa_ny = wa_dx + wa_x, wa_dy + wa_y
                if(0<=wa_nx<R and 0<=wa_ny<C and arr[wa_nx][wa_ny] != 'X' and arr[wa_nx][wa_ny] != 'D' and arr[wa_nx][wa_ny] != '*'):
                    wa_q.append((wa_nx,wa_ny))
                    arr[wa_nx][wa_ny] = '*'

        for _ in range(len(go_q)):
            go_x, go_y = go_q.popleft()
            for go_dx, go_dy in (-1,0),(1,0),(0,1),(0,-1):
                go_nx, go_ny = go_dx + go_x, go_dy + go_y

                if (go_nx == d_x and go_ny == d_y):
                    return v[go_x][go_y]

                if(0<=go_nx<R and 0<=go_ny<C and v[go_nx][go_ny] == 0) and (arr[go_nx][go_ny] == '.' or arr[go_nx][go_ny] == 'D'):
                    go_q.append((go_nx, go_ny))
                    v[go_nx][go_ny] = v[go_x][go_y] + 1


    return 'KAKTUS'

R,C = map(int, input().split())

arr = [list(input().strip()) for _ in range(R)]

S_index = deque()
W_index = deque()
D_index = deque()

v = [[0] * (C) for _ in range(R)]

for i in range(R):
    for j in range(C):
        x = arr[i][j]
        if  x == 'S':
            S_index.append((i,j))
            v[i][j] = 1
        if x == '*':
            W_index.append((i, j))
        if x == 'D':
            D_index.append((i, j))


print(bfs(S_index,W_index,D_index))
