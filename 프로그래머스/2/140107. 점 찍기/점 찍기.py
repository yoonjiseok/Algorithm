import math
def solution(k, d):
    
    ans = 0
    
    D = d**2
    for x in range(0,d+1,k):
        
        
        Y = (D - x**2)
        
        ans += int(math.sqrt(Y)) //k
        
        
        ans+=1
    
    
        
    return (ans)