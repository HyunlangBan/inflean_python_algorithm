n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = n

while True:
    mid = (end + start) // 2
    print(array[mid])
    if array[mid] < m:
        start = mid + 1
    elif array[mid] > m:
        end = mid - 1
    else:
        print(mid + 1)
        break
