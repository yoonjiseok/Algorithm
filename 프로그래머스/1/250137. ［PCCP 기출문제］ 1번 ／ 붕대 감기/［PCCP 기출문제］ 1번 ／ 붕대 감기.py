def solution(bandage, health, attacks):
    f_time = attacks[-1][0]
    
    con = 0
    
    x_h = health
    
    index = 0
    
    for i in range(f_time):
        # 공격 받았을 때
        if i + 1 == attacks[index][0]:
            x_h -= attacks[index][1]
            if x_h <= 0:
                return -1
            con = 0
            index += 1
            continue
        
        # 안받았을 때
        if x_h < health:
            if con == bandage[0] - 1:
                if x_h + bandage[1] + bandage[2] >= health:
                    x_h = health
                else:
                    x_h += bandage[1] + bandage[2]
                con = 0
            else:
                if x_h + bandage[1] >= health:
                    x_h = health
                else:
                    x_h += bandage[1]
                con += 1
        else:
            if con == bandage[0] - 1:
                con = 0
            else:
                con += 1
        
    
    
    return x_h