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


## Try 2 - ✅
n, k = map(int, input().split())
a = list(map(int, input().split()))

# a에서 3개를 뽑는다.
ch = [0]*n
res = [0]*3

total = set()

def DFS(L, idx):
  if L==3:
    total.add(sum(res))
    return

  for i in range(idx, len(a)):
    if ch[i] == 0:
      res[L] = a[i]
      ch[i] = 1
      DFS(L+1, i+1)
      ch[i] = 0

DFS(0, 0)
total = list(total)
total.sort(reverse=True)
# print(total)
print(total[k-1])
