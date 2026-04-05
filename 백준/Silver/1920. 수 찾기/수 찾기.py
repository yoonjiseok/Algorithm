import sys

input = sys.stdin.readline


X = int(input())
num1 = set(input().split())
Y = int(input())
num2 = (input().split())





for i in num2:
    if i in num1:
        print(1)
    else:
        print(0)