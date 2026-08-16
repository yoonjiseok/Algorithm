def solution(park, routes):
    def search(x,y,di,num):
        if di == 'N':
            if x - num < 0:
                return x,y
            
            for i in range(1,num+1):
                nx = x-i
                if park[nx][y] == 'X':
                    return x,y
            else:
                return x-num,y
            
            
        elif di == 'E':
            if y + num >= len(park[0]):
                return x,y
                
            for i in range(1, num+1):
                ny = y+i
                if park[x][ny] == 'X':
                    return x,y
            else:
                return x, y+num
            
            
        elif di == 'S':
            if x + num >= len(park):
                return x,y
            
            for i in range(1, num+1):
                nx = x+i
                if park[nx][y] == 'X':
                    return x,y
            else:
                return x+num, y
            
            
        else:
            if y - num < 0:
                return x,y
            for i in range(1,num+1):
                ny = y-i
                if park[x][ny] == 'X':
                    return x,y
            else:
                return x, y-num
            
    
    
    st_x = 0
    st_y= 0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                st_x = i
                st_y = j
                break
    
    for i in routes:
        di, num = i.split(' ')
        
        num = int(num)
        
        st_x, st_y = search(st_x,st_y,di,num)
    
    
    
    
    return st_x, st_y