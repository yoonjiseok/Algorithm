def solution(targets):
    
    targets.sort(key=lambda x: x[1])

    last_position = -1
    cnt = 0
    
    for i in range(len(targets)):
        
        if targets[i][0] >= last_position:
            cnt += 1
            last_position = targets[i][1]
                
    return cnt