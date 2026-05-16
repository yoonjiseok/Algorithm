import math

def get_lcm(a, b):
    return (a * b) // math.gcd(a, b)

def solution(signals):
    
    cycles = [i[0]+i[1]+i[2] for i in signals] 
    
    max_time = cycles[0]
    for i in range(1, len(cycles)):
        max_time = get_lcm(max_time, cycles[i])

    cnt = 1
    while cnt != max_time:
        for i in signals:
            sum_signal = i[0] + i[1] + i[2]
            rem = cnt % sum_signal

            if not (i[0] < rem <= i[0] + i[1]):
                break
        else:
            return cnt
        
        cnt += 1
    return -1
