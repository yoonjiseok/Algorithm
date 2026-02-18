import sys
input = sys.stdin.readline

M = int(input())

cnt = 1

st = 7

if M == 1:
    print(1)
    exit()

while True:
    if M <= st:
        print(cnt + 1)
        break
    else:
        cnt += 1
        st = st + (6* cnt)
