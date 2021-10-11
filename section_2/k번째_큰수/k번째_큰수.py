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

######## SOLUTION #########
## 3개를 뽑을때는 중복을 제거하면 안되었었는데 제거해서 결과 값이 다르게 나와버렸다. 
## set에서 add 쓰기

n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res = list(res)
res.sort(reverse=True)
print(res[k-1])
