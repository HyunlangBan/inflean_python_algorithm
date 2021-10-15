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

######### SOLUTION ###########
## lt, rt로 범위의 합을 비교하고 범위를 시킴 -> 더 간단!!

lt=0
rt=1
tot=a[0]
cnt=0

while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
        
print(cnt)
