import heapq

def solution(scoville, K):
    

    
    heapq.heapify(scoville)
    
    temp = 0
    cnt = 0
    while scoville[0] < K:
        if len(scoville) >= 2:
            x = heapq.heappop(scoville)
            y = heapq.heappop(scoville)
                
            temp = x+(y*2)
            heapq.heappush(scoville,temp)
            cnt+=1
        else:
            if scoville:
                X = heapq.heappop(scoville)
                if X >= K:
                    return cnt
                else:
                    return -1
            else:
                return -1        
            
    return cnt
