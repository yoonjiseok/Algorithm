from collections import deque
def solution(game_board, table):
    
    def normalize(block):
        min_x = min(b[0] for b in block)
        min_y = min(b[1] for b in block)
        
        return sorted([(b[0] - min_x, b[1] - min_y) for b in block])

    def rotate(block):
        
        rotate_block = [(b[1] , -b[0]) for b in block]
        return normalize(rotate_block)
        
    def search_1(x,y,idx):
        q = deque()
        q.append((x,y))
        v1[x][y] = idx
        D = []
        D.append((x,y))
        while q:
            x,y = q.popleft()
            
            for dx,dy in (-1,0),(0,1),(0,-1),(1,0):
                nx = dx + x
                ny = dy + y
                
                if (0<=nx<len(table) and 0<=ny<len(table[nx]) and table[nx][ny] == 1 and v1[nx][ny] == 0):
                    q.append((nx,ny))
            
                    v1[nx][ny] = idx
                    D.append((nx,ny))
        
        return D
    
    def search_0(x,y,idx):
        q = deque()
        q.append((x,y))
        v0[x][y] = idx
        D = []
        D.append((x,y))
        
        while q:
            x,y = q.popleft()
            
            for dx,dy in (-1,0),(0,1),(0,-1),(1,0):
                nx = dx + x
                ny = dy + y
                
                if (0<=nx<len(game_board) and 
                    0<=ny<len(game_board[nx]) and 
                    game_board[nx][ny] == 0 and 
                    v0[nx][ny] == 0):
                    
                    q.append((nx,ny))
                    
                    v0[nx][ny] = idx
                    D.append((nx,ny))
                    
        return D
                    
                    
    v1 = [[0]*len(table[0]) for _ in range(len(table))]
    v0 = [[0]*len(table[0]) for _ in range(len(table))]
    idx = 1
    
    table_1 = []
    game_board_0 = []
    
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == 1 and v1[i][j] == 0:
                table_1.append(search_1(i,j,idx))
                idx+=1
    
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 0 and v0[i][j] == 0:
                game_board_0.append(search_0(i,j,idx))
                idx+=1
                
    
    answer = 0
    used = [False] * len(table_1)
    
    for i in game_board_0:
        temp_i = normalize(i)
        matched = False
        
        for j,block in enumerate(table_1):
            if used[j] == True:
                continue
            if len(temp_i) != len(block):
                continue
            
            rotate_block = block
            
            for _ in range(4):
                rotate_block = rotate(rotate_block)
                
                if temp_i == rotate_block:
                    matched = True
                    used[j] = True
                    answer += len(rotate_block)
                    break
            
            if matched:
                break
        
                

    return answer