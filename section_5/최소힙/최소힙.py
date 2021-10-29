import heapq

h = []
res = []
while True:
  n = int(input())
  if n == -1:
    break
  elif n==0:
    ##### 추가 필요
    if len(a) == 0:
      print(-1)
    else:
    #####
      r = heapq.heappop(h)
      res.append(r)
  else:
    heapq.heappush(h, n)

for i in res:
  print(i)
