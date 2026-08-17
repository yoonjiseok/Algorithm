def solution(answers):
    num_1 = [1,2,3,4,5]
    num_2 = [2,1,2,3,2,4,2,5]
    num_3 = [3,3,1,1,2,2,4,4,5,5]
    
    idx = 0
    sc_1 = 0
    sc_2 = 0
    sc_3 = 0
    
    for i in answers:
        if num_1[idx % 5] == i:
            sc_1+=1
        if num_2[idx % 8] == i:
            sc_2 +=1
        if num_3[idx % 10] == i:
            sc_3 +=1
        
        idx+=1
    
    answer = []
    
    max_score = max(sc_1, sc_2, sc_3)
    
    if sc_1 == max_score:
        answer.append(1)
    if sc_2 == max_score:
        answer.append(2)
    if sc_3 == max_score:
        answer.append(3)
    
    
    
    
    
    
    
    return answer