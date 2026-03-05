from collections import deque
from collections import defaultdict

def solution(points, routes):

    v = defaultdict(int)
    
    
    for i in range(len(routes)):
        si,se = points[routes[i][0] - 1][0], points[routes[i][0] - 1][1]
        t = 0
        v[(t,si,se)] += 1
        for j in range(1,len(routes[i])):
            
            ei, ee = points[routes[i][j] - 1][0], points[routes[i][j] - 1][1]

            while si != ei:
                if si > ei:
                    t += 1
                    si -= 1
                    v[(t,si,se)] += 1
                else:
                    t += 1
                    si += 1
                    v[(t,si,se)] += 1

            while se != ee:
                if se > ee:
                    t += 1
                    se -= 1
                    v[(t,si,se)] += 1
                else:
                    t += 1
                    se += 1
                    v[(t,si,se)] += 1
        
    answer = 0
    for m in (v.values()):
        if m >= 2:
            answer+=1
    return answer