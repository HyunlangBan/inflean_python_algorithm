## visitied check를 안했음

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

#################### SOLUTION #####################

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
  global cnt
  if x==ex and y==ey:
    cnt += 1
  else:
    for k in range(4):
      xx=x+dx[k]
      yy=y+dy[k]
      if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>board[x][y]:
        ch[xx][yy]=1
        DFS(xx, yy)
        ch[xx][yy]=0 ##
        
n = int(input())
board = [[0]*n for _ in range(n)]
ch = [[0]*n for _ in range(n)]
max = -2147000000
min = 2147000000
for i in range(n):
  tmp = list(map(int, input().split()))
  for j in range(n):
    if tmp[j]<min:
      min=tmp[j]
      sx=i
      sy=j
    if tmp[j]>max:
      max=tmp[j]
      ex=i
      ey=j
    board[i][j]=tmp[j]
ch[sx][sy]=1
cnt=0
DFS(sx, sy)
print(cnt)


