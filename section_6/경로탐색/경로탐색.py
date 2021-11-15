## 풀이 방법 참고함
## OK

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
visited[0] = 1 ## missed
DFS(0)
print(cnt)


########### SOLUTION ##############

def DFS(v):
  global cnt
  if v == n:
    cnt += 1
#     for x in path:
#       print(x, end=' ')
#     print()
  else:
    for i in range(1, n+1):
      if g[v][i]== 1 and ch[i]==0:
        ch[i] = 1
#         path.append(i)
        DFS(i)
#         path.pop()
        ch[i]=0
        
n, m = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)]
ch = [0] * (n+1)
for i in range(m):
  a, b = map(int, input().split())
  g[a][b] = 1
cnt = 0
# path = []
# path.append(1)
ch[1] = 1
DFS(1)
