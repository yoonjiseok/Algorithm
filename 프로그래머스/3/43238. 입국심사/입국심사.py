def solution(n, times):
    
    left = 1
    right = max(times) * n
    
    
    answer = []
    
    while left <= right:
        mid = (right+left)//2
        temp = 0
        
        for i in times:
            temp += mid//i
        
        if temp >= n:
            right = mid -1
            answer.append(mid)

        else:
            left = mid + 1
            
    
    return min(answer)