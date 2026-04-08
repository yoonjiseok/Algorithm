from collections import defaultdict
def solution(id_list, report, k):
    

    
    singo_list = defaultdict(int)
    singo_id = set()
    rec_list = defaultdict(int)
    
    report = set(report)
    
    for i in report:
        x,y = i.split(' ')
        singo_list[x] += 1
        rec_list[y] += 1
        
                
            
    answer = defaultdict(int)


    for i in (id_list):
        if rec_list[i] >= k:
            for j in (id_list):

                if (j +' ' + i) in report:
                    answer[j] += 1
        
        
        
        
    real_answer = []
    for i in (id_list):
        real_answer.append(answer[i])
    
    return real_answer