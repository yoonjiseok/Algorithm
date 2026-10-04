from itertools import permutations

def solution(numbers):
    X = set()
    
    
    for i in range(1, len(numbers)+1):
        temp = permutations(numbers,i)
        
        for j in temp:
            temp_int= int(''.join(j))
                
            
            
            M = int((temp_int ** 0.5) + 1)
            
            if temp_int >=2:
                for k in range(2, M):
                    if temp_int %k == 0:
                        break
                else:
                    if temp_int not in X:
                        X.add(temp_int)
                
            
    
    return len(X)