from collections import deque
def solution(begin, target, words):
    
    def bfs(begin,target,words):
        q = deque()
        temp = 0
        q.append((begin,temp))
        
        while q:
            X,temp = q.popleft()
            
            if X == target:
                return temp
            
            for i in range(len(words)):
                cnt = 0
                for j in range(len(words[i])):
                    if X[j] == words[i][j]:
                        cnt+=1
                
                if cnt == len(X) - 1 and v[i] == 0:
                    q.append((words[i],temp+1))
                    v[i] = 1
        
    
        return 0
    
    v = [0] * (len(words) + 1)
    return bfs(begin,target,words)
    