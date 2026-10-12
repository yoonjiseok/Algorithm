import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0]) # 요청 시각 순 정렬
    
    hq = []
    answer = 0
    time = 0
    i = 0
    n = len(jobs)
    count = 0
    
    while count < n:
        # 현재 시간(time)까지 요청된 모든 작업을 힙에 추가
        while i < n and jobs[i][0] <= time:
            # 우선순위: 소요 시간(re)이 짧은 것, 요청 시각(st)이 빠른 것, 번호 순
            # 파이썬 튜플 정렬 특성상 (소요시간, 요청시각) 순으로 넣으면 됩니다.
            heapq.heappush(hq, (jobs[i][1], jobs[i][0]))
            i += 1
            
        if hq:
            # 힙에서 가장 소요 시간이 짧은 작업 꺼내기
            re, st = heapq.heappop(hq)
            time += re              # 현재 시간 갱신 (작업 소요 시간 만큼 증가)
            answer += (time - st)   # 반환 시간 누적
            count += 1
        else:
            # 만약 현재 시간에 처리할 수 있는 작업이 없다면, 
            # 다음 작업의 요청 시각으로 시간을 점프시킵니다.
            time = jobs[i][0]
            
    return answer // n