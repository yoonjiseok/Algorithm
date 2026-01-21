import sys
from collections import deque
input = sys.stdin.readline



def solve(O_arr, A_arr):
    q = deque()
    fin = int(A_arr[0])
    q.append((O_arr[0],''))


    ans = deque()
    while q:
        x,y = q.popleft()
        cx = int(x)


        if(cx==fin):
            print(y)
            break
        for dx in (cx*2 % 10000),(9999 if cx ==0 else cx-1), ((cx%1000)*10 + cx//1000 ), ((cx%10) * 1000 + cx//10):
            if dx == (cx*2 % 10000) and v[dx] == 0:
                v[dx] = 1
                q.append((dx, y+'D'))
            elif dx == (9999 if cx ==0 else cx-1) and v[dx] == 0:
                v[dx] = 1
                q.append((dx, y+'S'))
            elif dx == ((cx%1000)*10 + cx//1000 ) and v[dx] == 0:
                v[dx] = 1
                q.append((dx,y+'L'))
            elif dx == ((cx%10) * 1000 + cx//10) and v[dx] == 0:
                v[dx] = 1
                q.append((dx,y+'R'))



K = int(input())





for _ in range(K):
    v = [0] * 100000
    O_arr = list(deque())
    A_arr = list(deque())

    M,N = input().split()
    O_arr.append(M)
    A_arr.append(N)

    solve(O_arr, A_arr)

