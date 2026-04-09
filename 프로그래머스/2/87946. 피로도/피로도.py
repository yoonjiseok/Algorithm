def solution(k, dungeons):
    answer = 0
    visited = [0] * len(dungeons)
    
    def dfs(current_k, count):
        nonlocal answer
        
        answer = max(answer, count)
        
        for i in range(len(dungeons)):
            if not visited[i] and current_k >= dungeons[i][0]:
                visited[i] = True
                temp_k = current_k - dungeons[i][1]
                dfs(temp_k, count+1)
                
                visited[i] = False
    
    dfs(k,0)
    
    return answer