def bfs(si,sj,ei,ej):
    q = []
    q.append((si,sj))

    v[si][sj] = 1

    while q:
        x,y = q.pop(0)

        if ((x,y) == (ei, ej)):
            return v[x][y]

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = x+di, y+dj
            if (0<= ni < N and 0<= nj < M and adj[ni][nj] == 1 and v[ni][nj] == 0):
                q.append((ni,nj))
                v[ni][nj] = v[x][y] + 1



N,M = map(int, input().split())

adj = [list(map(int, input())) for _ in range(N)]


v = [[0] * M for _ in range(N)]

print(bfs(0,0,N-1,M-1))