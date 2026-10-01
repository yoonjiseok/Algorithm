def solution(x):
    x = str(x)
    
    temp = 0
    for i in x:
        i = int(i)
        temp+=i

    x = int(x)
    
    if x % temp ==0:
        return True
    else:
        return False
    