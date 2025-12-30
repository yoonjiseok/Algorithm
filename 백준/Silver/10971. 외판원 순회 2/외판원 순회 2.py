def dfs(cur,cnt,cost):
    global ans
    
    if cost > ans:
        return

    if cnt == N:
        if arr[cur][0] != 0:
            cost += arr[cur][0]
            ans = min(ans, cost)

    for i in range(N):
        if (v[i] == 0 and arr[cur][i] != 0):
            v[i] = 1
            dfs(i, cnt+1, cost + arr[cur][i])
            v[i] = 0

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
v = [0] * (N)

v[0] = 1
ans = float('inf')
dfs(0,1,0)
print(ans)
