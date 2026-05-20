def solution(n, w, num):
    answer = 0
    
    l_array = [[] for _ in range((n//w) + 1)]
    
    x = 1
    for i in range((n//w)+1):
        if i % 2 == 0:
            if i != 0:
                x += w + 1
            for j in range(w):
                l_array[i].append(x)
                x+=1
        else:
            x = (i+1) * (w)
            for j in range(w):
                
                l_array[i].append(x)
                x-=1
            
       
    for i in range((n//w)+1):
        for j in range(w):
            if l_array[i][j] == num:
                answer += 1
                cnt = i+1
                
                while cnt <= (n//w):
                    if l_array[cnt][j] <= n:
                        answer += 1
                        cnt += 1
                    else:
                        break
                
                return answer
                    
    
    return l_array