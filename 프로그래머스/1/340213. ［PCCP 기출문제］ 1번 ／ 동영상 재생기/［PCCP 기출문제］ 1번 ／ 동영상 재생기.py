def solution(video_len, pos, op_start, op_end, commands):
    op_s_h, op_s_m = op_start.split(':')
    op_e_h, op_e_m = op_end.split(':')
    
    op_start_time = int(op_s_h) * 60 + int(op_s_m)
    op_end_time = int(op_e_h) * 60 + int(op_e_m)
    
    
    pos_h, pos_m = pos.split(':')
    pos_time = int(pos_h)*60 + int(pos_m)
    
    vid_h, vid_m = video_len.split(':')
    video_time = int(vid_h)*60 + int(vid_m)
    
    for i in commands:
        if op_start_time <= pos_time <= op_end_time:
            pos_time = op_end_time
        
        if i == 'next':
            
            if pos_time >= video_time - 10:
                pos_time = video_time
            else:
                pos_time += 10
    
        else:
            if pos_time < 10:
                pos_time = 0
            else:
                pos_time -= 10
            
    if op_start_time <= pos_time <= op_end_time:
            pos_time = op_end_time
            
    h = pos_time // 60
    m = pos_time % 60
    
    
    
    
    if h < 10:
        h = str(h)
        h = '0' + h
    else:
        h = str(h)
    
    if m < 10:
        m = str(m)
        m = '0' + m
    else:
        m = str(m)
    

    answer = h+":"+m
    
    
    
    return answer