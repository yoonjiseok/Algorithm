def solution(plans):
    waiting = []
    q = {}
    
    for i in range(len(plans)):
        temp = plans[i][1].split(":")
        t1 = temp[0]
        t2 = temp[1]
        t1 = int(t1)
        t2 = int(t2)
        
        t = t1*60 + t2
        
        tl = plans[i][2]
        tl = int(tl)
        
        plans[i][1] = t
        plans[i][2] = tl
        
        q[plans[i][0]] = {'st' : t , 're' : tl}
    
    
    plans.sort(key=lambda x : x[1])
    
    time = plans[0][1]
    
    answer = []
    
    len_plans = len(plans)
    
    X,Y,Z = plans.pop(0)
    
    while len(answer) != len_plans:
        #plans 가 있다면
        if plans:
            t_X,t_Y,t_Z = plans.pop(0)
            
            #한번에 처리가 가능한지
            if Y+Z <= t_Y:
                answer.append(X)
                #대기하는 작업이 있는지
                if waiting:
                    
                    now = Y+Z
                    
                    while waiting:
                        w_X, w_Y, w_Z = waiting.pop()  
                        
                        if now+w_Z <= t_Y:
                            answer.append(w_X)
                            now = now+w_Z
                        else:
                            gap = t_Y - now
                            
                            waiting.append((w_X, t_Y, w_Z - gap))
                            break

                #대기하는 작없이 없다
                
                
                
                X,Y,Z = t_X,t_Y,t_Z
            
            #한번에 처리가 불가능함
            else:
                gap = t_Y - Y
                waiting.append((X,t_Y, Z-gap))
                X,Y,Z = t_X,t_Y,t_Z
        
        #plans가 없다면
        else:
            answer.append(X)
            while waiting:
                w_X, w_Y, w_Z = waiting.pop()

                answer.append(w_X)
                
            
            
            break
        
    
    return answer