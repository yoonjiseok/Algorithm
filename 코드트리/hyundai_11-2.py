N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 높이 오름차순으로 칸 정렬 (한 번만)
cells = sorted((grid[i][j], i, j) for i in range(N) for j in range(N))

def can_make_path(mid):
    dp = [[1] * N for _ in range(N)]   # (i,j)에서 끝나는 가장 긴 등산로 길이
    for h, x, y in cells:
        for dx, dy in ((-1,0),(0,1),(1,0),(0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                diff = h - grid[nx][ny]
                # 낮은 칸에서 올라오는 경우, 차이가 mid 이하일 때만
                if 0 < diff <= mid:
                    dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
        if dp[x][y] >= K:
            return True
    return False

left, right = 0, max(max(row) for row in grid)
answer = -1
while left <= right:
    mid = (left + right) // 2
    if can_make_path(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
