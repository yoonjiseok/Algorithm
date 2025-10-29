def bfs(c):
    x = map(int, str(c))
    sum = 0

    for i in x:
        sum += (i ** P)

    if(v[sum] == 3):
        return False

    v[sum] = v[sum] + 1


    arr[cnt+1] = sum
    return True

A, P = map(int, input().split( ))

arr = [0] *  300000
v = [0] * 300000

arr[0] = A
v[arr[0]] = 1

l = True

cnt = 0

while l:
    l = bfs(arr[cnt])
    cnt+=1

count = 0

for i in arr:
    if v[i] == 1:
        count +=1

print(count)