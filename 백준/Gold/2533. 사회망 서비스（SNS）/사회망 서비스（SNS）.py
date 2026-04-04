import sys

input = sys.stdin.readline

Q = int(input())

arr = [list(map(int,input().split())) for _ in range(Q-1)]

board = [[] for _ in range(Q+1)]

v = [0]*(Q+1)

z = 0
for i,j in arr:
    board[i].append(j)
    board[j].append(i)




sys.setrecursionlimit(10 ** 6)


dp = [[0, 0] for _ in range(Q + 1)]
visited = [False] * (Q + 1)


def dfs(node):
    visited[node] = True
    dp[node][0] = 0
    dp[node][1] = 1

    for child in board[node]:
        if not visited[child]:
            dfs(child)
            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child][0], dp[child][1])


dfs(1)
print(min(dp[1]))