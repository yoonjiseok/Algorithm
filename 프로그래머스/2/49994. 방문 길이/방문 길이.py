def solution(dirs):
    
    visited = set()
    
    x = 0
    y = 0
    
    cnt = 0
    for i in dirs:
        if i == 'U':
            nx = x+1
            ny = y
            
            if -5 <= nx <=5:
                if (nx,ny,x,y) not in visited:
                    visited.add((nx,ny,x,y))
                    visited.add((x,y,nx,ny))
                    
                    cnt+=1
                x = nx
                y = ny
            
        elif i == 'L':
            ny = y-1
            nx = x
            if -5 <= ny <=5:
                if (nx,ny,x,y) not in visited:
                    visited.add((nx,ny,x,y))
                    visited.add((x,y,nx,ny))
                    cnt+=1
            
                x = nx
                y = ny
                
        elif i == 'R':
            ny = y+ 1
            nx = x
            if -5 <= ny <=5:
                if (nx,ny,x,y) not in visited:
                    visited.add((nx,ny,x,y))
                    visited.add((x,y,nx,ny))
                    cnt+=1
                x = nx
                y = ny
               
            
        elif i == 'D':
            nx = x - 1
            ny = y
            if -5 <= nx <=5:
                if (nx,ny,x,y) not in visited:
                    visited.add((nx,ny,x,y))
                    visited.add((x,y,nx,ny))
                    cnt+=1
                x= nx
                y = ny

    return cnt