def solution(triangle):
    
    dp = [[0] * len(triangle[i]) for i in range(len(triangle))]
    
    dp[0][0] = triangle[0][0]
    
    dp[1][0] = triangle[1][0] + dp[0][0]
    dp[1][1] = triangle[1][1] + dp[0][0]
    
    for i in range(2,len(triangle)):
        for j in range(len(triangle[i])):
            #양끝은 예외처리
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
                
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                
            else:
                dp[i][j] = max(dp[i-1][j-1] , dp[i-1][j]) + triangle[i][j]
            
            
        
    answer = len(triangle) - 1
    
    return max(dp[answer])