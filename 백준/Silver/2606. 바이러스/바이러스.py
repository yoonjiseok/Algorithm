def dfs(adj):
    q = [0]
    cnt = 0

    while q:
        x = q.pop(0)

        for i in adj[x]:

            idx = i - 1
            if (v[idx] == 0):
                q.append(idx)
                v[idx] = 1
                cnt += 1

    print(cnt)

N = int(input())
V = int(input())

arr = [[] for _ in range(N+1)]

for _ in range(V):
    s,e = map(int,input().split())
    arr[s-1].append(e)
    arr[e-1].append(s)


v = [0] * (N+1)
v[0] = 1
dfs(arr)