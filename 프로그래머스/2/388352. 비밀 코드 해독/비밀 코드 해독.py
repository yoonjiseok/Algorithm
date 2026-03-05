from itertools import combinations
def solution(n, q, ans):
    answer = 0
    
    
    for c in combinations(range(1,n+1) , 5):
        is_valid = True
        for i in range(len(q)):
            sum_elements = set(c) & set(q[i])

            if ans[i] != len(sum_elements):
                is_valid = False
                break
            
        if is_valid == True:
            answer += 1
    
    return answer