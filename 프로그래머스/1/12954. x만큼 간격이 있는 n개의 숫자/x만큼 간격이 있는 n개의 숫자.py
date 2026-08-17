def solution(x, n):
    answer = []
    st = x
    for _ in range(n):
        answer.append(st)
        st += x
    
    return answer