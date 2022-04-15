# Try 1 - ✅

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

house = []
pizza = []
for i in range(n):
  for j in range(n):
    if city[i][j]==1:
      house.append((i, j))
    elif city[i][j]==2:
      pizza.append((i, j))
      
pizza_left = [0]*m
res = []
def DFS(L, idx):
  global res
  if L==m:
    sum_min_dis = 0
    for x, y in house:
      min_dis = 2147000000
      for k in range(m):
        a, b = pizza_left[k]
        dis = abs(x-a)+abs(y-b)
        if min_dis > dis:
          min_dis = dis
      sum_min_dis += min_dis
    res.append(sum_min_dis)
    return

  for i in range(idx, len(pizza)):
    pizza_left[L] = pizza[i]
    DFS(L+1, i+1)
    
DFS(0, 0)
res.sort()
print(res[0])
