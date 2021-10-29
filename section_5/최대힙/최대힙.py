import heapq

h = []
res = []
while True:
  n = int(input())
  if n == -1:
    break
  elif n==0:
    r = heapq.heappop(h)
    res.append(r)
  else:
    heapq.heappush(h, -n)

for i in res:
  print(-i)
