def solution(info, n, m):
    INF = float('inf')
    
    dp = [INF] * m
    
    dp[0] = 0
    
    for trace_a, trace_b in info:
        
        for j in range(m - 1, -1, -1):
            
            if dp[j] != INF:
                case_A = dp[j] + trace_a    
            else:
                case_A = INF
                
            if j >= trace_b and dp[j-trace_b] != INF:
                case_B = dp[j-trace_b]
            else:
                case_B = INF
                
            dp[j] = min(case_A, case_B)
    
        
    x = min(dp)
    
    if x < n:
        return x
    else:
        return -1
    