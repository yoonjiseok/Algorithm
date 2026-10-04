def solution(distance, rocks, n):
    
    rocks.sort()
    
    left = 0
    right = distance
    
    answer = []
    
    while left<= right:
        prev = 0
        cnt = 0
        temp_answer = []
        
        mid = (left + right) //2
        
        for i in rocks:
            if i - prev < mid:
                cnt +=1
            else:
                temp_answer.append(i-prev)
                prev = i
        
        if distance - prev < mid:
            cnt += 1
        
        if cnt <= n:
            answer.append(mid)
            left = mid+1
        else:
            right = mid -1
                
    
    
    return max(answer)