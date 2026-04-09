def solution(n):
    answer = 0
    visited = [0] * (n+1)
    
    
    def safe(current_row, col):
        for i in range(current_row):
            if visited[i] == col or abs(current_row - i) == abs(col - visited[i]):
                return True
        return False
    
    def dfs(current_row):
        nonlocal answer

        if current_row == n:
            answer += 1
            return
        
        
        for i in range(n):
            if safe(current_row, i):
                continue
            else:
                visited[current_row] = i
                dfs(current_row + 1)
                visited[current_row] = 0
    
    dfs(0)
    
    return answer