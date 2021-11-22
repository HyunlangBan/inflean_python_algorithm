n = int(input())
a = []
for _ in range(n):
  t, p = map(int, input().split())
  a.append((t, p))

def DFS(L, idx, t, p):
  global res
  if t == n:
    if p > res:
      res = p
    return

  for i in range(idx, n):
    t += a[i][0]
    p += a[i][1]
    next = i + a[i][0]
    DFS(L+1, next, t, p)
    t -= a[i][0]
    p -= a[i][1]

res = -2174000000
DFS(0, 0, 0, 0)
print(res)
