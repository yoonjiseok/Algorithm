def solution(grid):
    answer = []
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    def search(x,y,d):
        
        cnt= 0
        
        while True:
            if ((x,y,d)) in v:
                return cnt
            
            v.add((x,y,d))
            cnt += 1
            
            if grid[x][y] == 'L':
                d = (d-1) % 4
            elif grid[x][y] == 'R':
                d = (d+1) % 4
            
                
            x = (x + dx[d]) % X
            y = (y + dy[d]) % Y
            
                            
                        
                    
        
    
    # 싸이클의 기준은 첫 스타트 점이랑 방향이 같으면 싸이클인데, 
    # 그럼 각 점에서의 4방향을 다 계산하는건가
    
    array = [[0]*len(grid[0]) for _ in range(len(grid))]

    v = set()
    
    X = len(grid)
    Y = len(grid[0])
    
    
    for i in range(len(array)):
        for j in range(len(array[i])):
            for m in range(4):
                temp = search(i,j,m)
                if temp != 0:
                    answer.append(temp)
    
    answer.sort()
    return answer