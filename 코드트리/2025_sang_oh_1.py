import sys
from collections import deque
import heapq
input = sys.stdin.readline

def excute():
    e_temp_id_list = set()
    for i in range(N):
        for j in range(N):
            if new_board[i][j] != 0 :

                if i+1 != N and new_board[i][j] !=0 and new_board[i][j] != new_board[i+1][j]:
                    if new_board[i][j] < new_board[i + 1][j]:
                        e_temp_id_list.add((new_board[i][j],new_board[i+1][j]))
                    else:
                        e_temp_id_list.add((new_board[i+1][j],new_board[i][j]))

                if j+1 != N and new_board[i][j] != 0 and new_board[i][j] != new_board[i][j+1]:
                    if new_board[i][j] < new_board[i][j+1]:
                        e_temp_id_list.add((new_board[i][j],new_board[i][j+1]))
                    else:
                        e_temp_id_list.add((new_board[i][j+1], new_board[i][j]))

    sum = 0

    for i,j in e_temp_id_list:
        sum += width[i] * width[j]

    return sum

def move(idx):
    x1,y1,x2,y2 = position[idx]
    min_x,min_y = N,N
    max_x,max_y = 0,0
    temp_position = []
    is_found = False

    cnt = 0

    for i in range(y1,y2):
        for j in range(x1,x2):
            if board[i][j] == idx:
                cnt+=1
                if min_x > j:
                    min_x = j

                if min_y > i:
                    min_y = i

                if max_x <= j:
                    max_x = j

                if max_y <= i:
                    max_y = i


    for i in range(y1,y2):
        for j in range(x1,x2):
            if board[i][j] == idx:
                temp_position.append((i - min_y, j - min_x))



    W = max_x - min_x
    H = max_y - min_y


    new_board_position = []
    temp_cnt = 0
    is_found = False

    for nx in range(N):
        if nx+W >= N:
            continue
        if is_found:
            break
        for ny in range(N):

            if ny+H >= N:
                continue


            for dy,dx in (temp_position):
                if new_board[ny+dy][nx+dx] == 0:
                    temp_cnt += 1
                    new_board_position.append((ny+dy, nx+dx))
                else:
                    continue

            if cnt == temp_cnt:
                is_found = True
                position[idx] = (nx, ny, nx + W + 1, ny + H + 1)
                break
            else:
                new_board_position = []
                temp_cnt = 0

    if cnt == temp_cnt:
        for y,x in (new_board_position):
            new_board[y][x] = idx



def bfs(x,y,id):
    q = deque()
    q.append((x,y))
    v = [[0]*(N+1) for _ in range(N+1)]

    v[x][y] = 1
    cnt = 1
    while q:
        ax,ay = q.popleft()

        for dx,dy in (-1,0),(0,1),(0,-1),(1,0):
            nx,ny = ax+dx, ay + dy

            if (0<=nx<N+1 and 0<= ny <N+1 and v[nx][ny] == 0 and board[nx][ny] == id):
                q.append((nx,ny))
                v[nx][ny] = 1
                cnt += 1

    if width[id] != cnt:
        return False
    return True



N,Q = map(int, input().split())

board = [[0] * (N+1) for _ in range(N+1)]
arr = [list(map(int, input().split())) for _ in range(Q)]
id_list = set()

width  = [0] * (Q+1)

id = 1

position = [0] * (Q+2)

for i in range(Q):
    width_cnt = 0
    x1,y1,x2,y2 = arr[i]
    position[id] = (x1,y1,x2,y2)

    hq = []
    temp_id_list = set()

    for j in range(y1,y2):
        for l in range(x1,x2):
            if board[j][l] in id_list:
                temp_id = board[j][l]
                width[temp_id] -= 1
                temp_id_list.add(temp_id)

            board[j][l] = id
            width_cnt += 1

    for i in temp_id_list:
        tx1,ty1,tx2,ty2 = position[i]

        is_found = False

        for j in range(ty1, ty2):
            if is_found:
                break
            for l in range(tx1, tx2):
                if board[j][l] == i:
                    if not bfs(j,l,i):
                        is_found = True
                        width[i] = 0
                        break
                    else:
                        is_found = True
                        break


        if width[i] == 0:
            for j in range(ty1, ty2):
                for l in range(tx1, tx2):
                    if board[j][l] == i:
                        board[j][l] = 0

    id_list.add(id)
    width[id] = width_cnt

    for i in range(len(width)):
        if width[i] != 0:
            heapq.heappush(hq,(-width[i] , i))

    new_board = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(len(hq)):

        temp_width, temp_id = heapq.heappop(hq)
        move(temp_id)

    print(excute())

    board = new_board
    id += 1