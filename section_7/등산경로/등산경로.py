n = int(input())
g = []
min_n = 1e9
max_n = -2147000000
min_point = set()
max_point = set()

for i in range(n):
  a = list(map(int, input().split()))
  for j in range(n):
    if a[j] < min_n:
      min_n = a[j]
      min_point = (i, j)
    if a[j] > max_n:
      max_n = a[j]
      max_point = (i, j)

  g.append(a)

move = [(-1,0), (1, 0), (0, 1), (0, -1)]

def DFS(x, y):
  global cnt
  if x == max_point[0] and y == max_point[1]:
    cnt += 1
    return

  for a, b in move:
    n_x = x+a
    n_y = y+b
    if 0<=n_x<n and 0<=n_y<n and g[x][y] < g[n_x][n_y]:
      DFS(n_x, n_y)

cnt = 0
DFS(min_point[0], min_point[1])
print(cnt)
