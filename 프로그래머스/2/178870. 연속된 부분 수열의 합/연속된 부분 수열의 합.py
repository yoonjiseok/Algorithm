def solution(sequence, k):
    answer = []
    
    l = float('inf')
    left_n = 0
    right_n = 0
    
    sums = 0
    while left_n <= len(sequence):
        
        if sums < k:
            if right_n != len(sequence):    
                sums += sequence[right_n]
                right_n += 1
            else:
                break
            
        elif sums == k:
            
            if right_n - left_n < l:
                l = right_n - left_n
                answer = (left_n,right_n-1)
                
            if right_n == len(sequence):
                break
            sums = sums - sequence[left_n]
            left_n += 1
            
        elif sums > k:
            sums = sums - sequence[left_n]
            left_n += 1
        
    
    return answer