import sys
import heapq
input = sys.stdin.readline
from collections import defaultdict

X = int(input())

arr = [list(map(int, input().split())) for _ in range(X)]



mogi = defaultdict(int)


for i,j in arr:
    mogi[i] += 1
    mogi[j] -=1

current_mogi =0
max_mogi = 0

ans_st= 0
ans_end = 0
is_max_interval = False

for time in sorted(mogi.keys()):
    current_mogi +=mogi[time]

    if current_mogi > max_mogi:
        max_mogi = current_mogi
        ans_st = time
        is_max_interval = True

    elif current_mogi < max_mogi and is_max_interval:
        ans_end = time
        is_max_interval = False

print(max_mogi)
print(ans_st, ans_end)