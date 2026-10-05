from collections import deque
def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        temp_sum = 0
        for j in range(i,n+1):
            temp_sum += j
            
            if temp_sum == n:
                answer+=1
            elif temp_sum > n:
                break
    
    return answer