from collections import deque
def solution(n, computers):
    answer = 0
    v = [0] * n
    
    def bfs(l):
        q = deque()
        q.append(l)
        
        
        while q:
            x = q.popleft()
            for i in range(n):
                if v[i] == 0 and computers[x][i] == 1:
                    v[i] = 1
                    q.append(i)
    
    for i in range(n):
        if v[i] == 0:
            v[i] = 1
            bfs(i)
            answer += 1
            
    return answer