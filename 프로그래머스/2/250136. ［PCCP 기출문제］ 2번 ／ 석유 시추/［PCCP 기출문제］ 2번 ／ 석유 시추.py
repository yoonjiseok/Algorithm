from collections import deque

def solution(land):
    
    def bfs(X,Y,id):
        position = []
        q = deque()
        q.append((X,Y))
        v[X][Y] = id
        
        cnt = 1
        while q:
            x,y = q.popleft()
            
            for dx,dy in (-1,0),(0,1),(0,-1),(1,0):
                nx,ny = x+dx, y+dy
                if (0<=nx<n and 0<=ny<m and land[nx][ny] == 1 and v[nx][ny] == -1):
                    q.append((nx,ny))
                    v[nx][ny] = id
                    cnt += 1
        
        return cnt
        
    
    # 가로
    m = len(land[0])
    #세로
    n = len(land)
    
    answer = 0
    
    c_cnt =0
    Z = {}
    v = [[-1]*m for _ in range(n)]
    
    
    for i in range(m):
        id_list = set()
        m_cnt = 0
        for j in range(n):
            if land[j][i] == 1:
                
                
                if v[j][i] == -1:
                    temp = bfs(j,i,c_cnt)
                    
                    Z[c_cnt] = temp
                    c_cnt += 1
                temp_id = v[j][i]
                if temp_id not in id_list:
                                       
                    m_cnt += Z[temp_id]
                    id_list.add(temp_id)
                    
        if answer < m_cnt:
            answer = m_cnt
    
    return answer