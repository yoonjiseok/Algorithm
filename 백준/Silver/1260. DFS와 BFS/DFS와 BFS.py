def dfs(c):
    v[c] = 1
    ans_dfs.append(c)

    for i in adj[c]:
        if v[i] == 0:
            dfs(i)

def bfs(c):

    q = []
    q.append(c)
    l[c] = 1
    while q:
        z = q.pop(0)
        ans_bfs.append(z)

        for i in adj[z]:
            if l[i] == 0:
                q.append(i)
                l[i] = 1


N,M,V = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    s,e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

for i in range(1,N+1):
    adj[i].sort()

ans_dfs = []
ans_bfs = []

v = [0] * (N+1)
dfs(V)

l = [0] * (N+1)
bfs(V)

print(*ans_dfs)
print(*ans_bfs)