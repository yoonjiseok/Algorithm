def bfs(N,K):
    q = []
    q.append(N)

    while q:
        x = q.pop(0)

        next_position = [x+1, x-1, x*2]

        for next in next_position:
            if (0 <= next < len(v) and v[next] == 0):
                v[next] = v[x] + 1
                q.append(next)

N, K = map(int, input().split())

v = [0] * (200000)

if (N == K):
    print(0)
else:
    (bfs(N,K))
    print(v[K])