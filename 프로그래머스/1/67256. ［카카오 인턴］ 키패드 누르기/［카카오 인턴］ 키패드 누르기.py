from collections import deque
def solution(numbers, hand):
    
    phone = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  ['*', 0, '#']
]

    answer = ''
    l = [[3,0]]
    r = [[3,2]]
    
    
    
    def search(X, dist):
        q = deque()
        v = [[0] * 3 for _ in range(4)]
        
        
        st_x, st_y = X
        q.append((st_x,st_y,0))
        di_x, di_y = dist
        
        v[st_x][st_y] = 1
        
        while q:
            x,y,current_dist = q.popleft()
            
            if x == di_x and y == di_y:
                return current_dist
            
            for dx,dy in (-1,0), (1,0), (0,1), (0,-1):
                nx = dx+x
                ny = dy+y
                
                if (0<=nx<=3 and 0<=ny<=2 and v[nx][ny] == 0):
                    q.append((nx,ny,current_dist+1))
                    
             
        
    
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            if i == 1:
                l.append((0,0))
            elif i == 4:
                l.append((1,0))
            else:
                l.append((2,0))
        elif i in [3,6,9]:
            answer += 'R'
            
            if i == 3:
                r.append((0,2))
            elif i == 6:
                r.append((1,2))
            else:
                r.append((2,2))
        else:
            temp = []
            if i == 2:
                temp = (0,1)
            elif i == 5:
                temp = (1,1)
            elif i == 8:
                temp = (2,1)
            else:
                temp = (3,1)
            temp_l = search(l[-1], temp)
            temp_r = search(r[-1], temp)
            
            if temp_l == temp_r:
                if hand == "right":
                    answer += 'R'
                    r.append(temp)
                else:
                    answer += 'L'
                    l.append(temp)
            elif temp_l < temp_r:
                answer += 'L'
                l.append(temp)
            else:
                answer += 'R'
                r.append(temp)
       

    return answer