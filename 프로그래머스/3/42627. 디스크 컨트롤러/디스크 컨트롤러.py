import heapq
def solution(jobs):
    hq = []
    
    time = 0
    answer = []
    
    jobs.sort(key=lambda x:x[0])
    
    while jobs or hq:
        # 시작시간 + 작업시간 >= 다음 시작 시간 이면 waiting 에 포함.
        if jobs and not hq:
            st,re = jobs.pop(0)
            
            time = st + re
            
            while jobs:
                if st == jobs[0][0]:
                    temp_st, temp_re = jobs.pop(0)
                    if re > temp_st:
                        heapq.heappush(hq,(re,st))
                        
                        re = temp_re
                        time = st + re
                    else:
                        i,j = jobs.pop(0)
                        heapq.heappush(hq, (j,i))                  
                elif time >= jobs[0][0]:
                    i,j = jobs.pop(0)
                    heapq.heappush(hq, (j,i))
                else:
                    break
            
            answer.append(re)
        # hq 만 있을때
        elif hq and not jobs:
            re , st = heapq.heappop(hq)
            time += re
            answer.append(time - st)   
        # jobs 랑 hq 둘다 있을 때
        else:
            re , st = heapq.heappop(hq)
            time += re
            answer.append(time - st)
            
            while jobs:
                if time >= jobs[0][0]:
                    i,j = jobs.pop(0)
                    heapq.heappush(hq, (j,i))
                else:
                    break
            
            
            
        
        
    
    
    return sum(answer)//len(answer)