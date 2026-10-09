def solution(n, times):
    
    left = 1
    right = 0
    
    for i in times:
        right += n*i
    
    answer = []
    
    while left <= right:
        mid = (left+right) // 2
        
        temp = 0
        for i in times:
            temp += mid//i
            
        if temp < n:
            left = mid + 1
        
        if temp > n:
            right = mid -1
        
        if temp >= n:
            answer.append(mid)
            right = mid -1
            
    
    return min(answer)