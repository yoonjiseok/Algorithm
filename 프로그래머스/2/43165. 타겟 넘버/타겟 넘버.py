from collections import deque
def solution(numbers, target):
    
    def bfs(st):
        q = deque()
        idx = 0
        cnt = 0
        q.append((st,idx))
        q.append((-st, idx))
        
        while q:
            x,idx = q.popleft()
            
            if idx == len(numbers) - 1:
                
                if x == target:
                    cnt +=1
            
            if idx < len(numbers) -1:
                for dx in (numbers[idx+1]) , -(numbers[idx+1]):
                    nx = dx + x
                    
                    q.append((nx,idx+1))
        return cnt
    
    
    
    return bfs(numbers[0])
    
    