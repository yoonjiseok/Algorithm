from collections import deque

def solution(storage, requests):
    def bfs(word):
        q = deque()
        v[0][0] = 1
        q.append((0,0))
        temp = []
        cnt = 0
        while q:
            x,y = q.popleft()
    
            for dx,dy in (-1,0),(0,1),(0,-1),(1,0):
                nx,ny = x+dx, y+dy
                if (0<=nx<=N+1 and 0<=ny<=M+1 and grid[nx][ny] == '.' and v[nx][ny] == 0):
                    q.append((nx,ny))
                    v[nx][ny] = 1
        
        
        return v
    
    m_cnt = 0
    grid = [list(row) for row in storage]
    
    N = len(storage)
    M = len(storage[0])
    is_outside = [[0] * (M + 2) for _ in range(N + 2)]
    
    grid = [['.' for _ in range(M + 2)] for _ in range(N + 2)]
    
    for i in range(N):
        for j in range(M):
            grid[i + 1][j + 1] = storage[i][j]
    
    for i in range(len(requests)):
        if len(requests[i]) == 1:
            v = [[0] * (M + 2) for _ in range(N + 2)]

            is_outside = bfs(requests[i])
            
            for m in range(1,len(storage) + 1):
                for n in range(1, len(storage[0]) + 1):
                    if grid[m][n] == requests[i]:
                        for dx,dy in (-1,0),(0,1),(1,0),(0,-1):
                            x,y = dx+m, dy+n
                            if is_outside[x][y] == 1:
                                grid[m][n] = '.'
                                m_cnt += 1
                                break
                    
        else:
            for l in range(1,len(storage) + 1):
                for j in range(1,len(storage[0]) + 1):               
                    if grid[l][j] == requests[i][0]:
                        grid[l][j] = '.'
                        m_cnt += 1

    return (M*N) - m_cnt