def solution(rows, columns, queries):
    board = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]
    
    def search(x1,y1,x2,y2):
        x1-=1
        y1-=1
        x2-=1
        y2-=1
        
        r = []
        l = []
        a = []
        b = []
        
        #R
        for i in range(y1,y2):
            r.append(board[x1][i])
        
        #B
        for i in range(x1, x2):
            b.append(board[i][y2])
            
        #L
        for i in range(y2, y1,-1):
            l.append(board[x2][i])
        
        #A
        for i in range(x2,x1,-1):
            a.append(board[i][y1])
            
        
        r_min = min(r)
        b_min = min(b)
        l_min = min(l)
        a_min = min(a)
        
        for i in range(y1+1, y2+1):
            board[x1][i] = r.pop(0)
        
        for i in range(x1+1, x2+1):
            board[i][y2] = b.pop(0)
            
        
        for i in range(y2-1, y1-1,-1):
            board[x2][i] = l.pop(0)
                       
        for i in range(x2-1, x1-1,-1):
            board[i][y1] = a.pop(0)
            
        return min(r_min, b_min ,l_min, a_min)
        
        
    answer = []
    
    for i in queries:
        answer.append(search(i[0], i[1], i[2], i[3]))
        
    
    return answer