from collections import deque
def solution(plans):
    q = []
    st = {}
    re = {}
    answer = []
    
    for i in plans:
        h,m = i[1].split(":")
        h = int(h)
        m = int(m)
        d = i[2]
        d = int(d)
        
        t = h*60 + m
        
        st[i[0]] = t
        re[i[0]] = d
        
        i[1] = t
        i[2] = d
    
    plans.sort(key=lambda x:x[1])
    
    time = plans[0][1]
    
    
    while plans or q:            
        while plans:
            subject,start,duration = plans.pop(0)
            time = start
            if plans and time + duration > plans[0][1]:
                elapsed = plans[0][1] - time
                re[subject] -= elapsed
                time = plans[0][1]
                q.append(subject)
            else:
                # 현재 과제를 끝까지 마칠 수 있음
                time += duration
                answer.append(subject)
                
                # 과제를 끝낸 시각(time)에 멈춰둔 과제(q)를 처리할 수 있는지 확인
                while q:
                    if plans and time >= plans[0][1]:
                        break # 다음 새 과제 시작 시간이 되면 멈춤
                    
                    p_subject = q.pop()
                    
                    if plans and time + re[p_subject] > plans[0][1]:
                        # 멈춘 과제를 다 못 끝내면 남은 시간 갱신 후 다시 넣고 탈출
                        re[p_subject] -= plans[0][1] - time
                        time = plans[0][1]
                        q.append(p_subject)
                        break
                    else:
                        # 멈춘 과제를 다 끝낼 수 있음
                        time += re[p_subject]
                        answer.append(p_subject)
        # wating만 있을때
        while q:
            p_subject = q.pop()
            time += re[p_subject]
            answer.append(p_subject)
    
    return answer