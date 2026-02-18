import sys
input = sys.stdin.readline

arr = input().strip().upper()

answer = []


s1 = list(set(arr))

for x in s1:
    current = arr.count(x)
    answer.append(current)

m_max = max(answer)


if answer.count(m_max) > 1:
    print('?')
else:
    max_index = answer.index(m_max)
    print(s1[max_index])