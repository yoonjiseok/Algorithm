def solution(board, moves):
    stack = []
    stack_idx = 0
    
    def search(idx):
        for i in range(len(board)):
            if board[i][idx] != 0:
                return i
        
        return -1
    
    def bomb():
        temp_cnt = 0
        while True:
            if len(stack) >= 2:
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    temp_cnt += 2
                else:
                    return temp_cnt
            else:
                return temp_cnt
    
    cnt = 0
    for i in moves:
        b_idx = i-1
        x = search(b_idx)
        
        if x != -1:
            stack.append(board[x][b_idx])
            stack_idx += 1
            board[x][b_idx] = 0
        
        cnt += bomb()
        
    
    return cnt