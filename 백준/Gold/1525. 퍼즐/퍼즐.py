import sys
input = sys.stdin.readline
from collections import deque

def solve(arr,ans):
    q = deque()
    q.append(arr)

    while q:
        curr = q.popleft()
        zz = curr.find('0')
        x,y = zz // 3, zz % 3

        if (ans == curr):
            return 1

        for dx, dy in (-1,0),(1,0),(0,1),(0,-1):
            nx,ny = dx+x , dy+y

            if (0<=nx<3 and 0<=ny<3 ):

                t_index = nx*3 + ny

                o_index = x*3 + y

                s_list = list(curr)
                s_list[o_index], s_list[t_index] = s_list[t_index], s_list[o_index]
                next_string = "".join(s_list)

                if(next_string not in v):
                    v[next_string] = v[curr] + 1
                    q.append(next_string)

    return 0


arr = [list(map(int, input().split())) for _ in range(3)]
adj = ''
for i in range(3):
    for j in range(3):
        adj += str(arr[i][j])

ans = '123456780'

v = {}


v[adj] = 0
z = solve(adj,ans)
if z == 0:
    print(-1)
else:
    print(v[ans])
