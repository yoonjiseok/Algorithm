import sys
import heapq
input = sys.stdin.readline

head_id = None
tail_id = None

def can_complete(mid, ants):
    ants_cnt = 1

    curr_id = head_id

    start_pos = ant_house[curr_id]['position']

    while curr_id is not None:
        dist = ant_house[curr_id]['position'] - start_pos

        if dist > mid:
            ants_cnt += 1
            start_pos = ant_house[curr_id]['position']

        curr_id = ant_house[curr_id]['next_id']

    return ants_cnt<=ants

def add(ant_house_index, value):

    global tail_id

    ant_house[tail_id]['next_id'] = ant_house_index

    ant_house[ant_house_index] = {'position' : value ,
                                  'prev_id' : ant_house_index-1,
                                  'next_id' :  None}
    tail_id = ant_house_index


def rm(rm_index):

    global head_id, tail_id

    prev_id = ant_house[rm_index]['prev_id']
    next_id = ant_house[rm_index]['next_id']

    if prev_id is not None and next_id is not None:
        ant_house[prev_id]['next_id'] = next_id
        ant_house[next_id]['prev_id'] = prev_id


    elif prev_id is None and next_id is not None:
        head_id = next_id
        ant_house[next_id]['prev_id'] = None


    elif prev_id is not None and next_id is None:
        tail_id = prev_id
        ant_house[prev_id]['next_id'] = None


    elif prev_id is None and next_id is None:
        head_id = None
        tail_id = None

    del ant_house[rm_index]


def excute(ants):


    global head_id, tail_id

    low = 0
    high = ant_house[tail_id]['position'] - ant_house[head_id]['position']
    ans = high

    while low <= high:
        mid = (low + high)//2

        if can_complete(mid,ants):
            ans = mid
            high = mid-1
        else:
            low = mid+1

    print(ans)






Q = int(input())

arr = list(map(int, input().split()))

N = arr[1]

ant_house_index = 1

hq = []

ant_house = {}

for i in range(N):
    if ant_house_index == 1:
        ant_house[ant_house_index] = {'position' : arr[i + 2],
                                      'prev_id':None,
                                      'next_id' : ant_house_index + 1}
        head_id = ant_house_index
    elif i == N-1:
        ant_house[ant_house_index] = {'position': arr[i + 2],
                                      'prev_id': ant_house_index - 1,
                                      'next_id': None}
        tail_id = ant_house_index
    else:
        ant_house[ant_house_index] = {'position' : arr[i + 2],
                                      'prev_id': ant_house_index - 1,
                                      'next_id': ant_house_index + 1
                                      }
    ant_house_index += 1


for _ in range(Q-1):
    command, value = map(int, input().split())

    if command == 200:
        add(ant_house_index, value)
        ant_house_index += 1
    elif command == 300:
        rm(value)
    else:
        excute(value)