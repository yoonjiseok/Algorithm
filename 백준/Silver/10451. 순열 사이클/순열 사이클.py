def bfs(c):
    q = []
    q.append(c)


    while q:
        x = q.pop(0)

        if v[x] == 1:
            break

        q.append(arr[x-1])
        v[x] = 1




n = int(input())
for _ in range(n):
    m = int(input())

    arr = list(map(int, input().split()))

    cnt = 0

    v = [0] * (m+1)
    v[0] = 1

    for i in range(m):
        if v[arr[i]] == 1:
            continue
        bfs(arr[i])
        cnt += 1

    print(cnt)