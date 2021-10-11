n, p = map(int, input().split())
array = list(map(int, input().split()))

array = list(set(array))
result = []

for i in range(len(array) - 2):
    for j in range(i + 1, len(array) - 1):
        for k in range(j + 1, len(array)):
            sum = array[i] + array[j] + array[k]
            result.append(sum)


result = list(set(result))
result.sort(reverse=True)

print(result[p-1])

## 첫번째 예제만 맞춤...
