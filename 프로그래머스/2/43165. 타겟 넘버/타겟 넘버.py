from collections import deque
def solution(numbers, target):
    
    def bfs(st):
        q = deque()
        q.append((st,0))
        answer = 0
        while q:
            x,cnt = q.popleft()
            
            if cnt==len(numbers):
                if x == target:
                    answer += 1
            else:
            
                q.append((x-numbers[cnt],cnt+1))
                q.append((x+numbers[cnt], cnt+1))
            
            
        return answer
    
    return bfs(0)