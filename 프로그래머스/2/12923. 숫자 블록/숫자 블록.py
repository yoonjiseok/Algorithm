import math
def solution(begin, end):
    answer = [0] * (end-begin +1)
    
    t_begin = math.isqrt(begin)
    t_end = math.isqrt(end)
    n = 2
    
    for i in range(begin,end+1):
        temp_sqrt = math.isqrt(i)
        temp = 0

        is_found = False

        for j in range(2, temp_sqrt+1):
            if i % j ==0:
                if i//j <= 10000000:
                    temp = (i//j)
                    is_found = True
                    break
                else:
                    is_found = True
                    temp = j
        if is_found:     
            answer[i - begin] = (temp)
        else:
            answer[i - begin] = 1
    
    if begin == 1:
        answer[0] =0
    return answer