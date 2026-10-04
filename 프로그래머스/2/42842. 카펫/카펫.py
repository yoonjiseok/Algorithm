def solution(brown, yellow):
    
    w = 0
    h = 0
    while True:
        h +=1
        
        w = (brown+yellow)//h
        
        if  w <=0:
            continue
            
        if w >= h and ((w-2) * (h-2)) == yellow:
            return (w,h)
        
        
    