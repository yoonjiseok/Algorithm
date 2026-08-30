def solution(m, n, startX, startY, balls):
    #m 이 가로 n 이 세로
    answer = []
    
    def search(stX, stY, ball):
        dtX = ball[0]
        dtY = ball[1]
        
        #1 Y축 위로 이동
        temp1= abs(((n - dtY) + n) - stY)**2 + abs(dtX-stX)**2
        temp2 = abs(((m - dtX) + m) - stX)**2 + abs(dtY-stY)**2
        temp3 = abs(dtY + stY)**2 + abs(dtX-stX)**2
        temp4 = abs(stX + dtX)**2 + abs(dtY-stY)**2
        candidates = []
    
        if not (stX == dtX and stY < dtY):
            candidates.append(temp1)
            
    
        if not (stY == dtY and stX < dtX):
            candidates.append(temp2)
            
 
        if not (stX == dtX and stY > dtY):
            candidates.append(temp3)
            
    
        if not (stY == dtY and stX > dtX):
            candidates.append(temp4)
            
        return min(candidates)
        
            
        
    
    for i in balls:
        answer.append(search(startX,startY,i))
        
        
        
        
        
    
    return answer