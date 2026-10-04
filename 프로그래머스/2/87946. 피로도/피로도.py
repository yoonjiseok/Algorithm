from itertools import permutations
def solution(k, dungeons):
    
    answer = 0
    for p in permutations(dungeons, len(dungeons)):
        temp_k = k
        cnt = 0
        for i in p:
            if temp_k >= i[0]:
                temp_k -= i[1]
                cnt+=1
        
        if answer < cnt:
            answer = cnt
            
        
        
        
    return answer