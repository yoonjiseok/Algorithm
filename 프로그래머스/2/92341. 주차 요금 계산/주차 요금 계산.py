import math
from collections import defaultdict

def solution(fees, records):
    de_h = fees[0]
    de_cost = fees[1]
    per_m = fees[2]
    per_cost = fees[3]
    
    in_cars = []
    out_cars = []
    
   
    for i in records:
        if 'IN' in i:
            X,Y,Z = i.split(' ')
            in_h,in_m = X.split(':')
            in_h = int(in_h)
            in_m = int(in_m)
            in_t = in_h * 60 + in_m
            in_cars.append((in_t,Y))
        else:
            X,Y,Z = i.split(' ')
            out_h,out_m = X.split(':')
            out_h = int(out_h)
            out_m = int(out_m)
            out_t = out_h * 60 + out_m
            out_cars.append((out_t,Y))
    
    
    car_time = defaultdict(int) 
    
    for i in in_cars:
        is_found = False
        cnt = 0
        while cnt < len(out_cars):
            if i[1] == out_cars[cnt][1]:
                if i[0] <= out_cars[cnt][0]:
                    dur_time = out_cars[cnt][0] - i[0]
                    car_time[i[1]] += dur_time  
                    is_found = True
                    out_cars[cnt] = (-1, "USED") 
                    break
            cnt+=1
            
        if not is_found:
            dur_time = ((23*60)+59) - i[0]
            car_time[i[1]] += dur_time        

 
    answer = []
    

    for car_num in sorted(car_time.keys()):
        total_time = car_time[car_num]
        
        if total_time <= de_h:
            answer.append(de_cost) 
        else:
            
            cost = de_cost + math.ceil((total_time - de_h) / per_m) * per_cost
            answer.append(cost)

    return answer