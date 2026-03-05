from collections import defaultdict,deque

def solution(edges):
    
        
    Out = defaultdict(list)
    In = defaultdict(list)
    
    
    
    stick = 0
    new = 0
    palja = 0
    x_donut = 0
    for i in range(len(edges)):
        x,y = edges[i][0],edges[i][1]
        Out[x].append(y)
        In[y].append(x)
    all_node = set(Out) | set (In)
    
    for node in all_node:
        in_cnt = len(In[node])
        out_cnt = len(Out[node])
        
        if out_cnt>=2 and in_cnt == 0:
            new = node
        elif out_cnt == 0 and in_cnt >= 1:
            stick += 1
        elif in_cnt >=2 and out_cnt >= 2:
            palja += 1
        x_donut += in_cnt + out_cnt
    
            
    donut = len(Out[new]) - palja  - stick
    
    
    
    
    answer = [new, donut,stick, palja]
    # 도넛 나가는 간선 1개 들어오는 간선 1개
    # 막대 나가는 간선이 1개 들어오는 간선 O 개
    # 새로 생긴 노드 나가는 간선이 여러개 들어오는 간선 0개
    # 팔자는 들어오는 간선 2개 나가는 간선 2개 인 노드 세기

    return answer