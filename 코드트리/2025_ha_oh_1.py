import sys
from collections import deque

input = sys.stdin.readline

r_board_x = [-1,0,1,0]
r_board_y = [0,0,0,1]

b_board_x = [1,0,0,0]
b_board_y = [0,-1,0,1]

l_board_x = [-1,0,0,1]
l_board_y = [0,0,-1,0]

a_board_x = [-1,0,0,0]
a_board_y = [0,1,-1,0]

def sol(M, cleaner_grid):
    q = deque()
    q.append((M[0],M[1],0))
    v = [[0] * N for _ in range(N)]

    v[M[0]][M[1]] = 1

    candidates = []
    min_dist = float('inf')

    while q:
        x,y,dist = q.popleft()

        if dist > min_dist:
            continue
        if arr[x][y] >0:
            candidates.append((x,y))
            min_dist = dist

        if dist == min_dist:
            continue

        for dx,dy in (-1,0),(1,0),(0,1),(0,-1):
            nx,ny = dx+x, dy+y
            if (0<=nx<N and 0<=ny<N and v[nx][ny] == 0):
                if arr[nx][ny] != -1 and not cleaner_grid[nx][ny]:
                    q.append((nx,ny,dist+1))
                    v[nx][ny] = 1
    if candidates:
        candidates.sort(key=lambda c: (c[0], c[1]))
        return candidates[0][0], candidates[0][1]
    else:
        return M[0], M[1]
def clean(x,y):
    sum = []
    b_sum = 0
    for dx,dy in zip(r_board_x,r_board_y):
        nx,ny = dx+x, dy+y
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] > 0:
            b_sum += min(arr[nx][ny], 20)
    sum.append(b_sum)

    b_sum = 0
    for dx,dy in zip(b_board_x,b_board_y):
        nx,ny = dx+x, dy+y
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] > 0:
            b_sum += min(arr[nx][ny], 20)
    sum.append(b_sum)

    b_sum = 0
    for dx,dy in zip(l_board_x,l_board_y):
        nx,ny = dx+x, dy+y
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] > 0:
            b_sum += min(arr[nx][ny], 20)
    sum.append(b_sum)

    b_sum = 0
    for dx,dy in zip(a_board_x,a_board_y):
        nx,ny = dx+x, dy+y
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] > 0:
            b_sum += min(arr[nx][ny], 20)
    sum.append(b_sum)

    X = max(sum)
    X_index = sum.index(X)

    if X_index == 0:
        for dx,dy in zip(r_board_x,r_board_y):
            nx,ny = dx+x, dy+y

            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] != -1:
                    if arr[nx][ny] < 20 :
                        arr[nx][ny] = 0
                    else:
                        arr[nx][ny] = arr[nx][ny] - 20
    elif X_index == 1:
        for dx,dy in zip(b_board_x,b_board_y):
            nx,ny = dx+x, dy+y

            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] != -1:
                    if arr[nx][ny] < 20:
                        arr[nx][ny] = 0
                    else:
                        arr[nx][ny] = arr[nx][ny] - 20
    elif X_index == 2:
        for dx,dy in zip(l_board_x,l_board_y):
            nx,ny = dx+x, dy+y

            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] != -1:
                    if arr[nx][ny] < 20:
                        arr[nx][ny] = 0
                    else:
                        arr[nx][ny] = arr[nx][ny] - 20
    else:
        for dx,dy in zip(a_board_x,a_board_y):
            nx,ny = dx+x, dy+y

            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] != -1:
                    if arr[nx][ny] < 20:
                        arr[nx][ny] = 0
                    else:
                        arr[nx][ny] = arr[nx][ny] - 20


def add():
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                arr[i][j] += 5

def extend():
    temp = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                sum = 0
                for dx,dy in (-1,0),(0,1),(0,-1),(1,0):
                    nx,ny = dx+i, dy+j
                    if(0<=nx<N and 0<=ny<N and arr[nx][ny] > 0):
                       sum += arr[nx][ny]
                temp[i][j] = sum//10

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                arr[i][j] = temp[i][j]
N,K,L = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

cleaner = []
for _ in range(K):
    r, c = map(int, input().split())
    cleaner.append([r - 1, c - 1])

def end():
    sum = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] != -1 and arr[i][j] != 0:
                sum += arr[i][j]
    return sum


for _ in range(L):
    cleaner_grid = [[False] * N for _ in range(N)]
    for r,c in cleaner:
        cleaner_grid[r][c] = True

    for i in range(len(cleaner)):
        r,c = cleaner[i][0], cleaner[i][1]

        cleaner_grid[r][c] = False

        x,y = sol(cleaner[i],cleaner_grid)
        cleaner[i][0] = x
        cleaner[i][1] = y

        cleaner_grid[x][y] = True

    for i in range(len(cleaner)):
        clean(cleaner[i][0], cleaner[i][1])

    add()
    extend()
    print(end())