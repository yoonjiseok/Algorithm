import sys
input = sys.stdin.readline

def bfs(adj):
    q =  set([(0,0,adj[0][0])])
    r=0
    max_dist = 0
    while q:
        x,y,z = q.pop()
        max_dist = max(max_dist, len(z))

        if max_dist == 26:
            break


        for dx,dy in (-1,0) , (0,-1), (0,1), (1,0):
            nx, ny = x+ dx, y+dy

            if (0<=nx<M and 0<= ny<N and adj[nx][ny] not in z):
                q.add((nx,ny, z + adj[nx][ny]))
    print(max_dist)

M,N = map(int, input().split())

adj = [list(input().strip()) for _ in range(M)]


bfs(adj)
