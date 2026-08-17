def solution(n):
    ans = 2
    
    while True:
        if n%ans == 1:
            return ans
        ans +=1
    