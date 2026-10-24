N, K = map(int, input().split())
positions = list(map(int, input().split()))



positions.sort()

left = 1
right = positions[-1] - positions[0] + 1

answer = 0
while left <= right:
    temp = 0
    st = positions[temp]
    cnt = 1
    mid = (left + right) // 2
    temp_mid = mid

    # 지금 길이랑 개수로 커버가 다 가능할때
    
    for i in range(len(positions) - 1):
        length = positions[temp] + mid - 1

        if length >= positions[i+1]:
            continue
        else:
            temp = i+1
            cnt+=1

    if cnt > K:
        left = mid + 1
    if cnt <= K:
        answer = mid
        right = mid -1
    
print(answer)

    
    
    # 지금 길이랑 개수로 커버가 불가능할때



# Please write your code here.
