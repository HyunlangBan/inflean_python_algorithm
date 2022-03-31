## Try 1 - ✅
n = int(input())
c = []
for _ in range(n):
  c.append(int(input()))

res = 2147000000
def DFS(L, x, y, z):
  global res
  if L == n:
    if x!=y and y!=z and x!=z:
      max_sum = max(x, y, z)
      min_sum = min(x, y, z)
      res = min(res, (max_sum-min_sum))
    return

  DFS(L+1, x+c[L], y, z)
  DFS(L+1, x, y+c[L], z)
  DFS(L+1, x, y, z+c[L])

DFS(0, 0, 0, 0)
print(res)
