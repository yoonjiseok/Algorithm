from collections import deque
def solution(x, y, n):
    def bfs(x,y,n):
        cnt = 0
        q = deque()
        q.append((x,cnt))
        v[x] = 1
        
        while q:
            x,cnt = q.popleft()
            
            if x == y:
                return cnt
            
            for dx in (x+n), (x*2),(x*3):
                if (dx <= y and v[dx] == 0):
                    v[dx] = 1
                    q.append((dx,cnt+1))
            
        return -1
    
    v = [0] * (y + 1)
    
    answer = bfs(x,y,n)
    
    
    return answer
    
    
    