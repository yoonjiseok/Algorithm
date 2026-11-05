from collections import defaultdict
def solution(id_list, report, k):
    
    report_dict_y = {}
    report_dict_x = {}
    
    for i in id_list:
        report_dict_y[i] = 0
        report_dict_x[i] = []
        
    a = set()
    
    for i in report:
        x,y = i.split(' ')

        if (x,y) in a:
            continue
        else:
            report_dict_y[y] += 1
            report_dict_x[x].append(y)
            a.add((x,y))
        
    answer = []
    for i in id_list:
        Y = report_dict_x[i]
        
        cnt = 0
        for j in Y:
            if report_dict_y[j] >= k:
                cnt+=1
        
        answer.append(cnt)
    
    return answer