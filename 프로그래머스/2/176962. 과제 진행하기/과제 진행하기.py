def solution(plans):
    
    subject = {}
    stack = []
    answer = []
    cnt = 0

    plans.sort(key=lambda x : x[1])
    for i in plans:
        h = int(i[1][0:2]) * 60
        m = int(i[1][3:])
        
        subject[cnt] = {'subject':i[0] , 'start' : h+m, 't':int(i[2])}
        cnt += 1
        
  

    for i in range(len(plans)-1):
        id, start, play_time = i,subject[i]['start'], subject[i]['t']
        next_start = subject [i+1]['start']
        available_time = next_start - start
        
        if play_time <= available_time:
            answer.append(subject[id]['subject'])
            available_time = available_time - play_time
            
            
            while available_time > 0 and stack:
                temp_id, temp_time = stack.pop()
                
                if available_time >= temp_time:
                    available_time -= temp_time
                    answer.append(subject[temp_id]['subject'])
                else:
                    temp_time -= available_time
                    stack.append((temp_id, temp_time))
                    break

        else:
            rest_time = play_time - available_time
            stack.append((id,rest_time))        
    
    answer.append(plans[-1][0])
    while stack:
        id, re_time = stack.pop()
        answer.append(subject[id]['subject'])
            
            
            
            
            
    return answer