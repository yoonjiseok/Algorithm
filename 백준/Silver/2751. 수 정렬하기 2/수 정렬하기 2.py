import sys

input = sys.stdin.readline

X = int(input())

answer = []
for _ in range(X):
    N = int(input())
    answer.append(N)

answer.sort()

for i in answer:
    print(i)