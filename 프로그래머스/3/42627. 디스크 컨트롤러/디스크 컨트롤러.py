import heapq
def solution(jobs):

    jobs.sort(key=lambda x:x[0])
    
    i = 0
    n = len(jobs)
    answer = []
    hq = []
    time = 0
    
    while i<n or hq:
        while i<n and time >= jobs[i][0]:
            heapq.heappush(hq,(jobs[i][1] , jobs[i][0]))
            i +=1
        
        if hq:
            re,st = heapq.heappop(hq)
            time += re
            answer.append(time-st)
            
            
        else:
            time = jobs[i][0]
    
    
    return sum (answer) // len(answer)