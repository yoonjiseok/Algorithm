import sys
import heapq
input = sys.stdin.readline


N, K = map(int, input().split())

J_arr = [list(map(int, input().split())) for _ in range(N)]

B_arr = [int(input()) for _ in range(K)]
hq = []

J_arr.sort(key=lambda x: x[0])


B_arr.sort()
answer = 0

cap_j = []

J_idx = 0
for bag in B_arr:
    temp = []
    while J_idx < N and bag >= J_arr[J_idx][0]:
        heapq.heappush(cap_j,(-J_arr[J_idx][1]))
        J_idx+=1
    if cap_j:
        answer += -heapq.heappop(cap_j)


print(answer)


