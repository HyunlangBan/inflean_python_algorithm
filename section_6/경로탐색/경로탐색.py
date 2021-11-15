n, m = map(int, input().split())

g = [[0]*n for _ in range(n)]
visited = [0]*n
for _ in range(m):
  x, y = map(int, input().split())
  g[x-1][y-1] = 1

def DFS(node):
  global cnt
  if node == (n-1):
    cnt += 1
    return
  visited[node] = 1
  a = g[node]
  for i in range(n):
    if a[i] and not visited[i]:
      DFS(i)
      visited[i] = 0

cnt = 0
DFS(0)
print(cnt)
