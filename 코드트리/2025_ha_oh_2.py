import sys
import math
import heapq
input = sys.stdin.readline


def cal_max_gap():
    while hq:

        current_max = hq[0]
        l_node = current_max[1]
        r_node = current_max[2]

        if right_node.get(l_node) != r_node:
            heapq.heappop(hq)
        else:
            return current_max

    return None

def add():
    x = cal_max_gap()


    new_node = math.ceil((x[2] + x[1]) /2)

    garo.append(new_node)

    left_node[new_node] = x[1]
    right_node[new_node] = x[2]

    right_node[x[1]] = new_node
    left_node[x[2]] = new_node

    cp_garo.append(new_node)

    heapq.heappush(hq, (-(new_node - x[1]), x[1], new_node ))
    heapq.heappush(hq, (-(x[2] - new_node) , new_node, x[2]))
    return

def rm(y):
    global head_val, tail_val
    rm_value = cp_garo[y]

    l = left_node.get(rm_value)
    r = right_node.get(rm_value)

    if l is not None:
        right_node[l] = r
    else:
        head_val = r

    if r is not None:
        left_node[r] = l
    else:
        tail_val = l

    if l is not None and r is not None:
        heapq.heappush(hq, (-(r - l), l, r))

    left_node.pop(rm_value, None)
    right_node.pop(rm_value, None)

R = int(input())

garo = []

left_node = {}
right_node = {}

hq = []

st = list(map(int, input().split()))


for i in range(3,len(st)):
    garo.append(st[i])

    if i==3:
        right_node[st[i]] = st[i+1]
    elif i==len(st)-1:
        left_node[st[i]] = st[i-1]
    else:
        left_node[st[i]] = st[i-1]
        right_node[st[i]] = st[i+1]



en_point = st[1]
st_point = 1

garo = sorted(list(set(garo)))

cp_garo = [0] + garo[:]

head_val = garo[0]
tail_val = garo[-1]

for i in range(len(garo) - 1):
    x = -(right_node[garo[i]] - garo[i])
    heapq.heappush(hq, (x, garo[i], right_node[garo[i]]))


for _ in range(R-1):
    command_line = list(map(int, input().split()))
    x = command_line[0]

    if x == 400:
        m_max = (cal_max_gap())
        max_gap = -m_max[0] if m_max else 0

        start_gap = (head_val - st_point) * 2

        end_gap = (en_point - tail_val) * 2

        print(max(max_gap, start_gap, end_gap))

    elif x == 200:
        add()
    elif x == 300:
        y = command_line[1]
        rm(y)

