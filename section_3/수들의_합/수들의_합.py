n, m = map(int, input().split())
array = list(map(int, input().split()))

cnt = 0
for i in range(n):
    sum = array[i]
    if sum > m:
        continue
    idx = i
    while sum<m and idx < n-1:
        sum += array[idx+1]
        idx += 1
    if sum == m:
        cnt += 1
print(cnt)
