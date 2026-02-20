import sys
import heapq
input = sys.stdin.readline

def request(id,p,r):
    ships[id] = {'p' : p, 'r' : r, 'ready_time' : 0}
    heapq.heappush(hq, (-p, id))
    ship_id_list.append(id)

def change(id, p):
    ships[id]['p'] = p
    heapq.heappush(hq,(-p, id))


def attack():
    sum = 0
    cnt = 0
    ship_id_list = []

    temp = []
    while hq and cnt<5:
        p, ship_id = heapq.heappop(hq)
        p = -p

        if cnt==5:
            return sum, cnt, ship_id_list
        if ships[ship_id]['p'] == p:
            if ships[ship_id]['ready_time']  > 0:
                temp.append((-p, ship_id))
                continue
            else:
                sum += p
                ships[ship_id]['ready_time'] = ships[ship_id]['r']
                ship_id_list.append(ship_id)
                temp.append((-p, ship_id))

                cnt+=1
        else:
            continue
    for item in temp:
        heapq.heappush(hq, item)

    return sum, cnt, ship_id_list

def time_update():
    for i in ship_id_list:

        if ships[i]['ready_time'] > 0:
            ships[i]['ready_time'] -= 1
        else:
            continue

N = int(input())

time = 0

command_line = list(map(int, input().split()))
command = command_line[0]

hq = []
ship_id_list = []
ships = {}

cnt = 2
for i in range(command_line[1]):

    ship_id = command_line[cnt]
    p = command_line[cnt+1]
    r = command_line[cnt+2]
    ships[ship_id] = {'p' : p, 'r' : r, 'ready_time' : 0}
    heapq.heappush(hq,(-p, ship_id))
    ship_id_list.append(ship_id)
    cnt+=3



for _ in range(N-1):
    command_line = list(map(int, input().split()))
    command = command_line[0]

    if command == 200:
        id = command_line[1]
        p = command_line[2]
        r = command_line[3]
        request(id,p,r)
        time_update()

    elif command == 300:
        id = command_line[1]
        p = command_line[2]

        change(id,p)
        time_update()
    elif command == 400:


        x,y,z = attack()
        print(x,y,*z)
        time_update()
