from collections import deque
n, m, k = map(int, input().split())

edges = []

array = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    edges.append((x - 1, y - 1))
    array[x].append(y)
    

start_points = list(map(lambda x: int(x), input().split()))


def search(st):
    q = deque()
    q.append(st)

    v[st] = 1
    idx = 0

    while q:
        x = q.popleft()

        for nx in (array[x]):
            
            if v[nx] == 0:
                v[nx] = v[x] + 1
                q.append(nx)

    return v

temp = []
for i in start_points:
    v = [0] * (n+1)
    temp.append(search(i))
    
min_of_max_t = float('inf')

for i in range(1, n + 1):  
    current_max_t = 0
    can_reach_all = True
    
    for j in range(k):
   
        if temp[j][i] == 0:
            can_reach_all = False
            break
            
        current_max_t = max(current_max_t, temp[j][i])
        

    if can_reach_all:

        if min_of_max_t > current_max_t:
            min_of_max_t = current_max_t

if min_of_max_t == float('inf'):
    print(-1)
else:
    print(min_of_max_t - 1)

