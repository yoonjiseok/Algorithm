import sys
from collections import deque
input = sys.stdin.readline
def turn_left(d):
    if d==1:
        return 4
    elif d==2:
        return 3
    elif d==3:
        return 1
    elif d==4:
        return 2

def turn_right(d):
    if d == 1:
        return 3
    elif d == 2:
        return 4
    elif d == 3:
        return 2
    elif d == 4:
        return 1



def ans():
    q = deque()
    cnt = 0
    q.append((st_po[0],st_po[1],st_po[2],cnt))

    v[st_po[2]][st_po[0]][st_po[1]] = 1

    while q:
        x,y,d,cnt = q.popleft()


        if(x==dt_po[0] and y==dt_po[1] and d==dt_po[2]):
            return cnt


        if d == 1:
            # y 값을 1씩 늘려야 함.
            for dy in range(1,4):
                ny=y+dy
                if (ny < 0 or ny >= M or arr[x][ny] == 1):
                    break
                if (0<=ny<M and arr[x][ny] == 0 and v[d][x][ny] == 0 and arr[x][ny] == 0):
                    q.append((x,ny,d,cnt+1))
                    v[d][x][ny] = 1
        elif d == 2:
            # y 값을 1씩 줄여야 함.
            for dy in range(1,4):
                ny=y-dy
                if (ny < 0 or ny >= M or arr[x][ny] == 1):
                    break
                if (0<=ny<M and arr[x][ny] == 0 and v[d][x][ny] == 0 and arr[x][ny] == 0):
                    q.append((x,ny,d,cnt+1))
                    v[d][x][ny] = 1
        elif d == 3:
            # x 값을 1씩 줄여야 함.
            for dx in range(1,4):
                nx=x+dx
                if (nx < 0 or nx >= N or arr[nx][y] == 1):
                    break
                if (0<=nx<N and arr[nx][y] == 0 and v[d][nx][y] == 0 and arr[nx][y] == 0):
                    q.append((nx,y,d,cnt+1))
                    v[d][nx][y] = 1
        elif d == 4:
            # x 값을 1씩 늘려야 함.
            for dx in range(1,4):
                nx=x-dx
                if (nx < 0 or nx >= N or arr[nx][y] == 1):
                    break
                if (0<=nx<N and arr[nx][y] == 0 and v[d][nx][y] == 0 and arr[nx][y] == 0):
                    q.append((nx,y,d,cnt+1))
                    v[d][nx][y] = 1

        nd_left = turn_left(d)
        if (v[nd_left][x][y] == 0):
            q.append((x,y,nd_left,cnt+1))
            v[nd_left][x][y] = 1

        nd_right = turn_right(d)
        if (v[nd_right][x][y] == 0):
            q.append((x,y,nd_right,cnt+1))
            v[nd_right][x][y] = 1



N, M = map(int , input().split())

arr = [list(map(int , input().split())) for _ in range(N)]

st_po = list(map(int, input().split()))
dt_po = list(map(int, input().split()))

for i in range(0,2):
    st_po[i] -= 1
    dt_po[i] -= 1


v = [[[0]*M for _ in range(N)] for _ in range(5)]

print(ans())