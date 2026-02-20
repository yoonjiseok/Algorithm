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

def process_cooldown():
    while cooldown_hq and cooldown_hq[0][0] <= current_time:
        ready_time, sid = heapq.heappop(cooldown_hq)
        heapq.heappush(hq, (-ships[sid]['p'], sid))

def attack():
    total_p = 0
    cnt = 0
    ship_id_list = []

    while hq and cnt<5:
        p, ship_id = heapq.heappop(hq)
        p = -p

        if ships[ship_id]['p'] != p:
            continue

        if ships[ship_id]['ready_time'] > current_time:
            continue
        else:
            total_p += p
            ships[ship_id]['ready_time'] = current_time +  ships[ship_id]['r']
            heapq.heappush(cooldown_hq, (ships[ship_id]['ready_time'] , ship_id))

            ship_id_list.append(ship_id)

            cnt += 1

    return total_p, cnt, ship_id_list



N = int(input())

current_time = 0

command_line = list(map(int, input().split()))
command = command_line[0]

hq = []
cooldown_hq = []
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

current_time += 1

for _ in range(N-1):
    command_line = list(map(int, input().split()))
    command = command_line[0]

    process_cooldown()

    if command == 200:
        id = command_line[1]
        p = command_line[2]
        r = command_line[3]
        request(id,p,r)


    elif command == 300:
        id = command_line[1]
        p = command_line[2]

        change(id,p)

    elif command == 400:


        x,y,z = attack()
        print(x,y,*z)
    current_time += 1
