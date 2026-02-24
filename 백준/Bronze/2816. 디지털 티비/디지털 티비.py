import sys

input = sys.stdin.readline


def bfs(kbs1, kbs2):
    x = 0
    answer = []

    while True:
        # 1. 종료 조건
        if kbs1 == 0 and kbs2 == 1:
            return answer


        if kbs1 != 0:
            if x < kbs1:

                if arr[x] != 'KBS1' and arr[x] != 'KBS2':

                    answer.append(3)
                    arr[x], arr[x + 1] = arr[x + 1], arr[x]


                    if arr[x] == 'KBS1': kbs1 = x
                    if arr[x] == 'KBS2': kbs2 = x
                    x += 1
                elif arr[x] == 'KBS2':

                    answer.append(1)
                    x += 1

            elif x == kbs1:

                answer.append(4)
                arr[x], arr[x - 1] = arr[x - 1], arr[x]

                if arr[x] == 'KBS2': kbs2 = x
                x -= 1
                kbs1 = x

            else:

                answer.append(2)
                x -= 1

        else:
            if x < kbs2:

                if arr[x] != 'KBS1' and arr[x] != 'KBS2':

                    answer.append(3)
                    arr[x], arr[x + 1] = arr[x + 1], arr[x]

                    if arr[x] == 'KBS2': kbs2 = x
                    x += 1
                elif arr[x] == 'KBS1':

                    answer.append(1)
                    x += 1

            elif x == kbs2:

                answer.append(4)
                arr[x], arr[x - 1] = arr[x - 1], arr[x]
                x -= 1
                kbs2 = x

            else:
                answer.append(2)
                x -= 1



N = int(input())
arr = [input().rstrip() for _ in range(N)]

kbs1 = 0
kbs2 = 0

for i in range(N):
    if arr[i] == 'KBS1':
        kbs1 = i
    if arr[i] == 'KBS2':
        kbs2 = i


print(''.join(map(str, bfs(kbs1, kbs2))))