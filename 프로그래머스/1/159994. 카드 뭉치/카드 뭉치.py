def solution(cards1, cards2, goal):
    c1_idx = 0
    c2_idx = 0
    g_idx = 0
    
    for word in goal:
        if c1_idx < len(cards1) and cards1[c1_idx] == word:
            c1_idx+=1
        elif c2_idx < len(cards2) and cards2[c2_idx] == word:
                c2_idx+=1
        else:
            return "No"
        
    return "Yes"
        
