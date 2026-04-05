import sys

input = sys.stdin.readline
q = []

X = int(input())

for _ in range(X):
    command_line = input().strip()

    if 'push' in command_line:
        Y,num = command_line.split(' ')
        q.append(num)
    else:
        if command_line == 'front':
            if len(q) == 0:
                print(-1)
            else:
                print(q[0])
        elif command_line == 'back':
            if len(q) == 0:
                print(-1)
            else:
                print(q[-1])
        elif command_line == 'size':
            print(len(q))
        elif command_line == 'pop':
            if len(q) == 0:
                print(-1)
            else:
                print(q.pop(0))
        elif command_line == 'empty':
            if len(q) == 0:
                print(1)
            else:
                print(0)