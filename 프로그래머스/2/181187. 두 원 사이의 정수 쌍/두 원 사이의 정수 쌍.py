import math

def solution(r1, r2):
    cnt = 0

    r22 = r2**2
    r11 = r1**2
    
    for x in range(1,r2):
        
        max_r = r22 - x**2 
        min_r = r11 - x**2
        
        if min_r <= 0:
            
            max_r = math.sqrt(max_r)
            max_r = math.floor(max_r)
            cnt += max_r
        else:
        
            max_r = math.sqrt(max_r)
            min_r = math.sqrt(min_r)

            max_r = math.floor(max_r)
            min_r = math.ceil(min_r)

            cnt += max_r - min_r + 1
        
    cnt *= 4
    
    cnt2 = r2-r1+1
    cnt2 *= 4
    
    
    return(cnt+cnt2)
    
    
    