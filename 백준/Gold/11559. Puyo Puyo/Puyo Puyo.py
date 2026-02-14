import sys
input = sys.stdin.readline
from collections import deque

def arranged():
    for j in range(6):
        puyos = deque()
        for i in range(12):
            if arr[i][j] != '.':
                puyos.append(arr[i][j])

        for i in range(12 - len(puyos)):
            arr[i][j] = '.'

        for i in range(12 - len(puyos), 12):
            arr[i][j] = puyos.popleft()

def ans(st,si):
    q = deque()
    q.append((st,si))

    boom_temp = deque()

    st_word = arr[st][si]
    v[st][si] = 1
    cnt = 1
    while q:
        x,y = q.popleft()

        for dx,dy in (-1,0),(1,0),(0,1),(0,-1):
            nx,ny = dx+x, dy+y
            if(0<=nx<12 and 0<=ny<6 and v[nx][ny] == 0 and arr[nx][ny] != '.'):
                if(arr[nx][ny] == st_word):
                    q.append((nx,ny))
                    boom_temp.append((nx,ny))
                    v[nx][ny] = 1
                    cnt+=1

    if len(boom_temp) >= 3:
        for x,y in boom_temp:
            visited.append((x,y))
    return cnt



arr = [list(map(str, input().strip())) for _ in range(12)]



solution = 0


while True:
    v = [[0] * 6 for _ in range(12)]
    visited = []
    is_boom = False
    for i in range(6):
        for j in range(12):
            if (v[j][i] == 0 and arr[j][i] != '.'):
               if ans(j,i) >= 4:
                    visited.append((j,i))
                    is_boom = True

    if not is_boom:
        break
    else:
        for x, y in visited:
            arr[x][y] = '.'
        solution+=1
        arranged()
print(solution)