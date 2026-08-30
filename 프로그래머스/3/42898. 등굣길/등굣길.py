def solution(m, n, puddles):
    s_p = set()
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for i in puddles:
        s_p.add(tuple(i))
    
    dp[1][1] = 1
    for i in range(1,n+1):
        
        for j in range(1,m+1):
            if i == 1 and j ==1:
                continue
            if (j,i) not in s_p:
                if (j,i-1) in s_p:
                    dp[i][j] = dp[i][j-1]
                elif (j-1,i) in s_p:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    
    print(dp)
    answer = 0
    return dp[n][m]