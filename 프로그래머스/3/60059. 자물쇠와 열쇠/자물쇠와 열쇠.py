def rotate_90(arr):
    M = len(arr)
    temp_array = [[0] * M for _ in range(M)]
    
    for i in range(M):
        for j in range(M):
            temp_array[j][M - 1 - i] = arr[i][j]
            
    return temp_array


def check(new_lock, N):
    for i in range(N):
        for j in range(N):
         
            if new_lock[N + i][N + j] != 1:
                return False
    return True

def solution(key, lock):
    N = len(lock)
    M = len(key)
    

    new_lock = [[0] * (N * 3) for _ in range(N * 3)]
    

    for i in range(N):
        for j in range(N):
            new_lock[N + i][N + j] = lock[i][j]
            
    
    for _ in range(4):
        key = rotate_90(key) 
        
        
        for x in range(N * 2):
            for y in range(N * 2):
                
                
                for i in range(M):
                    for j in range(M):
                        new_lock[x + i][y + j] += key[i][j]
                        
                if check(new_lock, N):
                    return True              
                    
                
                for i in range(M):
                    for j in range(M):
                        new_lock[x + i][y + j] -= key[i][j]
                        
    
    return False
    