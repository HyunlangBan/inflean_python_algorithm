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


############ SOLUTION ############
## BFS

from collections import deque

MAX = 100000
ch = [0] * (MAX+1)
dis = [0] * (MAX+1)
n, m = map(int, input().split())
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)

while dQ:
  now = dQ.popleft()
  if now==m:
    break
  for next in (now-1, now+1, now+5):
    if 0<next<=MAX:
      if ch[next] == 0:
        dQ.append(next)
        ch[next]=1
        dis[next]=dis[now]+1
        
print(dis[m])
