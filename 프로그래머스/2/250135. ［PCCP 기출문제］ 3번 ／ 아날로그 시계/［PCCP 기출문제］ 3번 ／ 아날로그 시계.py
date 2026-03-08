def solution(h1, m1, s1, h2, m2, s2):

    
    s_1 = h1*3600 + m1 * 60 + s1
    s_2 = h2*3600 + m2 * 60 + s2
    
    a_h = 360 / (3600*12)
    a_m = 360 / 3600  
    a_s = 360 / 60
    
    answer = 0

    if s_1 == 0 or s_1 == 43200:
            answer += 1
    while s_1 < s_2:

        cur_h = (s_1 * a_h) % 360
        cur_m = (s_1 * a_m) % 360
        cur_s = (s_1 * a_s) % 360
        
        next_h = ((s_1 + 1) * a_h) % 360
        next_m = ((s_1 + 1) * a_m) % 360
        next_s = ((s_1 + 1) * a_s) % 360
        
        if next_h == 0 : next_h = 360
        if next_m == 0 : next_m = 360
        if next_s == 0 : next_s = 360
        
        
        if next_s == 360 and next_m == 360 and next_h == 360:
            answer -= 1
        
        if cur_s < cur_m and next_s >= next_m:
            answer += 1
        if cur_s < cur_h and next_s >= next_h:
            answer += 1

        s_1 += 1
    
    
    
    
    return answer