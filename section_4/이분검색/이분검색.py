n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = n

while True:
    mid = (end + start) // 2
    if array[mid] < m:
        start = mid + 1
    elif array[mid] > m:
        end = mid - 1
    else:
        print(mid + 1)
        break
        
# sort 안함
# while 조건 틀림


############ SOLUTION ##############

a.sort()
lt = 0
rt = n-1

while lt <= rt:
    mid = (lt+rt)//2
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt = mid-1
    else:
        lt = mid+1
       
