def solution(today, terms, privacies):
    
    period = {}
    t_y,t_m,t_d = today.split('.')
    
    
    t_y = int(t_y)
    t_m = int(t_m)
    t_d = int(t_d)
    
    for i in terms:
        x,y = i.split(' ')
        y = int(y)
        y = y * 28 -1
        
        period[x] = y
    
    idx = 1
    answer = []
    
    t_total = t_y * 12 * 28 + t_m * 28 + t_d
    
    for i in privacies:
        x,y = i.split(' ')
        
        #sort = 6*28
        sort = period[y]
        
        p_y,p_m,p_d = x.split('.')
        
        
        p_y = int(p_y)
        p_m = int(p_m)
        p_d = int(p_d)
        
        p_d += sort
        
        p_total = p_y * 12 * 28 + p_m * 28 + p_d
        
        
        if t_total > p_total:
            answer.append(idx)
        
        idx += 1
    
    
    return answer