import sys

input = sys.stdin.readline


X = int(input())

stack = []

for _ in range(X):
    command_line = input().strip()
    if 'push' in command_line:
        L,num = command_line.split(' ')
        stack.append(num)

    else:
        if command_line == 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
        elif command_line == 'size':
            print(len(stack))
        elif command_line == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif command_line == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
