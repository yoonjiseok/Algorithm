import heapq
def solution(n, works):
    answer = 0
    
    
    hq = []
    
    for i in (works):
        heapq.heappush(hq,-i)
    
    
    while n!=0:
        X = heapq.heappop(hq)
        
        if X != 0:
            X += 1
        heapq.heappush(hq, X)
        
        n -= 1
            
    
    for i in hq:
        answer += i **2
    return answer