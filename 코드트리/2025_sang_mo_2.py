import sys
from collections import deque
import heapq
input = sys.stdin.readline

def bfs(si,st,ei,et):
    INF = float('inf')
    q = []
    k = 1
    heapq.heappush(q,(0,k,si,st))


    v = [[[INF] * (N+1) for _ in range(N+1)] for _ in range(6)]
    v[k][si][st] = 0


    while q:
        t_time, k,x,y = heapq.heappop(q)

        if x == ei and y == et:
            return t_time

        if v[k][x][y] < t_time:
            continue

        if k<5:
            next_time = (k+1)**2 + t_time
            if v[k+1][x][y] > next_time:
                v[k+1][x][y] = next_time
                heapq.heappush(q,(next_time, k+1, x,y))

        for i in range(1,k):
            next_time = t_time +1
            if v[i][x][y] > next_time:
                v[i][x][y] = next_time
                heapq.heappush(q,(t_time + 1, i , x, y))



        for dx,dy in (-k,0), (k, 0), (0, k),(0,-k):
            nx,ny = x+dx,y+dy

            if (0<=nx<N and 0<= ny < N and 0<k<6):
                is_safe = False
                if dx == -k or dx == k:
                    step = 1 if nx > x else -1
                    for i in range(x +step ,nx + step ,step):
                        if board[i][ny] == '#':
                            is_safe = True
                            break
                if dy == -k or dy == k:
                    step = 1 if ny > y else -1
                    for i in range(y + step ,ny + step ,step):
                        if board[nx][i] == '#':
                            is_safe = True
                            break

                if is_safe:
                    continue


                if (board[nx][ny] != '#' and board[nx][ny] != 'S'):
                    next_time = t_time + 1
                    if v[k][nx][ny] > next_time:
                        v[k][nx][ny] = next_time
                        heapq.heappush(q,(next_time, k, nx, ny))


    return -1
N = int(input())

board = [list(map(str, input().strip())) for _ in range(N)]


Q = int(input())


for _ in range(Q):
    si,st,ei,et = map(int, input().split())

    print(bfs(si - 1,st - 1,ei - 1,et - 1))
