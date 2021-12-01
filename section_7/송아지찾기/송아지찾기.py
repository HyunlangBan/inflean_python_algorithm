s, e = map(int, input().split())

distance = e-s
move = [5, 1, -1]
def DFS(p, c):
  global res
  if c > res:
    return
  if p > e:
    return
  if p == e:
    if c < res:
      res = c
    return
  
  for m in move:
    p += m
    c += 1
    DFS(p, c)
    p -= m
    c -= 1

res = 1247000000
DFS(s, 0)

print(res)
