def solution(diffs, times, limit):
    
    high = max(diffs)
    low = 1
    answer = 0
    mid = (high + low)//2
    
    while low<=high:
        mid = (high + low)//2
        x_sum = 0
        
        for i in range(len(diffs)):
            if mid >= diffs[i]:
                x_sum += times[i]
            else:
                if i != 0:
                    x_sum += (times[i-1] + times[i])*(diffs[i] - mid) + times[i]
                else:
                    x_sum += times[0]
            
        if x_sum > limit:
            low = mid + 1
        else:
            answer = mid
            high = mid - 1
    
        
    return answer