n, m = map(int, input().split())
# 눈의 합 중 가장 확률이 높은 숫자
size = n+m+1
array = [0] * size

for i in range(1, n+1):
    for j in range(1, m+1):
        array[i+j] += 1

max_count = max(array)

for i in range(len(array)):
    if array[i] == max_count:
        print(i, end=' ')
        
