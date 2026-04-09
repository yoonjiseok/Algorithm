def solution(n, computers):
    answer = 0
    v = [0] * n
    
    def dfs(x):

        v[x] = 1 
        for i in range(n):
            if computers[x][i] == 1 and v[i] == 0:

                dfs(i)
                
                
    
    for i in range(n):
        if v[i] == 0:
            dfs(i) 
            answer += 1
            
    return answer