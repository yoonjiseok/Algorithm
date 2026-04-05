import sys

input = sys.stdin.readline


X = int(input())

num = []

for _ in range(X):
    x,y = map(int,input().split(' '))

    num.append((x,y))

num.sort(key=lambda x: (x[0],x[1]))

for i,j in num:
    print(i , j)