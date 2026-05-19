def solution(friends, gifts):
    gift_score = {}
    gift_record = {}
    
    for i in friends:
        gift_record[i] = {}
        gift_score[i] = {}
        gift_score[i] = 0
        for j in friends:
            if i != j:
                gift_record[i][j] = 0
                 
    
    
    for i in gifts:
        sender, receiver = i.split(' ')
        
        gift_record[sender][receiver] += 1
        
    
    for i in friends:
        cnt = 0
        for j in gifts:
            sender, receiver = j.split(' ')
            if i == sender:
                gift_score[sender] += 1
            if i == receiver:
                gift_score[receiver] -= 1
                
    
    answer = []
    
    
    
    for i in friends:
        cnt = 0
        for j in friends:
            if i != j:
                if gift_record[i][j] > gift_record[j][i]:
                    cnt += 1
                elif gift_record[i][j] == gift_record[j][i]:
                    if gift_score[i] > gift_score[j]:
                        cnt+=1
        answer.append(cnt)
                    
                
                    
            
    
    return max(answer)