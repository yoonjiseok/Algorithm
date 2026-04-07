import sys,heapq


input = sys.stdin.readline


X= int(input())

max_hq = []
min_hq = []

cnt = 0

mid = 0
for _ in range(X):
    N = int(input())

    if len(max_hq) == len(min_hq):
        heapq.heappush(max_hq,-N)
    else:
        heapq.heappush(min_hq,N)

    if min_hq and -max_hq[0] > min_hq[0]:
        x = -heapq.heappop(max_hq)
        y = heapq.heappop(min_hq)

        heapq.heappush(max_hq, -y)
        heapq.heappush(min_hq,x)

    print(-max_hq[0])

