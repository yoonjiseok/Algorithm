def bfs(si,sj,ei,ej,R):
    q = []
    q.append((si,sj))
    while q:
        x,y = q.pop(0)


        for di,dj in (-1,0),(0,-1),(1,0),(0,1):
            ni, nj = x + di , y + dj
            if (0 <= ni <= ei and 0<= nj <= ej and v[ni][nj] == 0 and arr[ni][nj] > R):
                q.append((ni,nj))
                v[ni][nj] = 1


N = int(input())

arr = [list(map(int, input().split( ))) for _ in range(N)]
solution = []

max_num = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] > max_num:
            max_num = arr[i][j]

count = 0
for k in range(0, max_num+1):
    v = [[0] * N for _ in range(N+1)]
    answer = []
    count = 0
    for i in range(N):
        for j in range(N):
            if(v[i][j] == 0 and arr[i][j] > k):
                bfs(i,j,N-1,N-1, k)
                count = count + 1

    solution.append(count)

print(max(solution))
