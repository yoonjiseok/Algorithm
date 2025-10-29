def bfs(si,sj,ei,ej):
    q = []
    cnt = 1
    q.append((si,sj))
    v[si][sj] = 1

    while q:
        x,y = q.pop(0)

        for di, dj in (-1,0),(1,0),(0,-1),(0,1):
            ni,nj = x + di, y+dj

            if (0 <= ni <= ei and 0 <= nj <= ej and v[ni][nj] == 0 and adj[ni][nj] == 1):
                q.append((ni,nj))
                v[ni][nj] = 1
                cnt+=1

    return cnt



N = int(input())
p = []
adj = [list(map(int, input())) for _ in range(N)]
v = [[0] * (N+1) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if (v[i][j] == 0 and adj[i][j] == 1):
            p.append(bfs(i, j, N - 1, N - 1))

print(len(p))
p.sort()
for i in p:
    print(i)