from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    v = [[0] * m for _ in range(n)]
    
    
    def bfs(st,si,et,ei):
        q = deque()
        q.append((st,si))
        v[st][si] = 1
        
        while q:
            x,y = q.popleft()
            if x == et and y == ei:
                    return v[x][y]
            
            for dx,dy in (-1,0),(1,0),(0,1),(0,-1):
                nx,ny = x+dx,y+dy
                
                
                
                if(0<=nx<=et and 0<=ny<=ei and v[nx][ny] == 0 and maps[nx][ny] == 1):
                    q.append((nx,ny))
                    v[nx][ny] = v[x][y] + 1
                    
        return -1
    
    return(bfs(0,0,n-1,m-1))
    