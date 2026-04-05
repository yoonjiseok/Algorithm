def solution(picks, minerals):
    answer = 0
    
    strees = []
    
    cnt = 0
    sum = 0
    mine = ''
    X = 0
    for i in picks:
        X += i*5
    
    if X < len(minerals):      
        minerals = minerals[:X]
    
    for i in range(0, len(minerals), 5):
        chunk = minerals[i:i+5]
        
        sum_val = 0
        mine = ""
        for m in chunk:
            if m == 'diamond':
                sum_val += 25
                mine += 'd'
            elif m == 'iron':
                sum_val += 5
                mine += 'i'
            else:
                sum_val += 1
                mine += 's'
                
        strees.append((sum_val, mine))
    
    st = 0
    answer = 0
    strees.sort(key = lambda x: x[0],reverse=True)
    Y = len(strees)
    i = 0
    for i in range(len(strees)):
        

        while st < 3 and picks[st] == 0:
            st += 1
            

        if st == 3:
            break
            
  
        if st == 0:
            for j in strees[i][1]:
                answer += 1
        elif st == 1:
            for j in strees[i][1]:
                if j == 'd': answer += 5
                else: answer += 1
        elif st == 2:
            for j in strees[i][1]:
                if j == 'd': answer += 25
                elif j == 'i': answer += 5
                else: answer += 1

        picks[st] -= 1
    
    
    return answer