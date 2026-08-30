def solution(n):
    if n%2 != 0:
        return 0
    dp = [0]*(n+1)
    dp[0] = 1
    
    
    for i in range(2,n+2,2):
        if i == 2:
            dp[i] = 3
        else:
            
            dp[i] = dp[i-2] * 3
                     
            for j in range(i-4, -1, -2):
                dp[i] += dp[j] * 2
                
            dp[i] %= 1000000007
            
        
    
    
    return dp[n]