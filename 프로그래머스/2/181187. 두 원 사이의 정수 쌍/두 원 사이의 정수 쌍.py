import math
def solution(r1, r2):
    
    max_ans = 0
    min_ans = 0
    
    R1 = r1**2
    R2 = r2**2
    
    for x in range(r1+1):
        Y = R1 - x**2
        y = math.isqrt(Y)
        
        if y * y == Y :
            min_ans -= 1
        
        min_ans += 1
            
        min_ans += int(y)
        
    
    for x in range(0, r2+1):
        Y = R2 - x**2
        
        if x == 0:
            max_ans -= r2-r1 + 1
        max_ans += int(math.isqrt(Y))
        max_ans +=1
    
            
    print(max_ans)
    print(min_ans)
    
    answer = 0
    return (max_ans-min_ans) * 4