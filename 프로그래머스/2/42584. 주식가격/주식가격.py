def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        if i != len(prices):
            for j in range(i+1, len(prices)):
                if prices[i] <= prices[j]:
                    cnt += 1
                else:
                    cnt += 1
                    break
            answer.append(cnt)
        else:
            answer.append(0)            
        
            
    return answer