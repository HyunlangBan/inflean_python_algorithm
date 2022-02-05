## Try 1 - ❌
## 미리 sort 해봤자 더하면 소용이 없구나..
n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

cnt = 0
res = set()
for i in range(n):
  for j in range(i+1, n):
    for m in range(j+1, n):
      res.add(a[i]+a[j]+a[m])

res = list(res)
print(res[k-1])
