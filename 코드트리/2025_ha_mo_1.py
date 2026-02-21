import sys
from collections import deque
input = sys.stdin.readline
import heapq

packages = {}

def move(L):
    id,h,w,c= L

    temp_x = N

    is_find = False
    for i in range(1, N+1):
        if is_find:
            break
        for j in range(c, c+w):
            if (board[i][j] != 0 and board[i][j] != id):
                temp_x = i
                is_find = True
                break

    top = temp_x -h
    bottom = temp_x - 1
    left_col = c
    right_col = c+w -1

    packages[id] = {
        'top' : top,
        'bottom' : bottom,
        'left_col' : left_col,
        'right_col' : right_col
    }
    for i in range(temp_x - h , temp_x):
        for j in range(c, c+w):
            board[i][j] = id



def apply_gravity():
    sorted_id = sorted(packages.keys(), key=lambda x: packages[x]['bottom'], reverse=True)

    for pid in sorted_id:
        p_info = packages[pid]
        top = p_info['top']
        bottom = p_info['bottom']
        left_col = p_info['left_col']
        right_col = p_info['right_col']

        h = bottom - top + 1

        for i in range(top, bottom +1):
            for j in range(left_col, right_col+1):
                board[i][j] = 0

        new_bottom = bottom

        for i in range(bottom+1, N+1):
            is_blocked=False

            for j in range(left_col, right_col+1):
                if board[i][j] != 0:
                    is_blocked = True
                    break

            if is_blocked:
                break
            else:
                new_bottom = i

        new_top = new_bottom -h + 1

        for i in range(new_top, new_bottom +1):
            for j in range(left_col, right_col+1):
                board[i][j] = pid

        packages[pid]['top'] = new_top
        packages[pid]['bottom'] = new_bottom



def left(id):
    pid = packages[id]
    top = pid['top']
    bottom = pid['bottom']
    left_col = pid['left_col']
    right_col = pid['right_col']


    for i in range(top, bottom+1):
        for j in range(left_col, right_col +1):
            board[i][j] = 0

    del packages[id]

    apply_gravity()

    return id



def right(id):
    pid = packages[id]

    top = pid['top']
    bottom = pid['bottom']
    left_col = pid['left_col']
    right_col = pid['right_col']


    for i in range(top, bottom+1):
        for j in range(left_col, right_col +1):
            board[i][j] = 0

    del packages[id]

    apply_gravity()

    return id








N,M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]

board = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    move(arr[i])

cnt = 0
while packages:
    temp_id = float('inf')

    # left
    for i in packages.keys():
        is_blocked = False

        for j in range(packages[i]['top'], packages[i]['bottom']+1):
            for k in range(packages[i]['left_col']):
                if (board[j][k] != 0):
                    is_blocked = True
                    break
            if is_blocked:
                break

        if not is_blocked:
            if temp_id > i:
                temp_id = i
    left(temp_id)
    print(temp_id)

    #Right
    temp_id = float('inf')
    for i in packages.keys():
        is_blocked = False

        for j in range(packages[i]['top'], packages[i]['bottom'] + 1):
            for k in range(packages[i]['right_col']+1, N+1):
                if (board[j][k] != 0):
                    is_blocked = True
                    break
            if is_blocked:
                break

        if not is_blocked:
            if temp_id > i:
                temp_id = i

    right(temp_id)
    print(temp_id)



