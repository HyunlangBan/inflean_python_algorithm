g = []

for _ in range(7):
  a = list(map(int, input().split()))
  g.append(a)

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def DFS(x, y):
  global cnt
  if x==6 and y==6: 
    cnt += 1
    return

  for a, b in move:
    n_x = x+a
    n_y = y+b
    if 0<=n_x<7 and 0<=n_y<7 and g[n_x][n_y]==0:
      g[n_x][n_y]=1
      DFS(n_x, n_y)
      g[n_x][n_y]=0
    

cnt = 0
g[0][0]=1      ### 이걸 빼먹음!
DFS(0,0)
print(cnt)


############ SOLUTION ############

def DFS(x, y):
  global cnt
  if x==6 and y==6:
    cnt += 1
  else:
    for i in range(4):
      xx = x+dx[i]
      yy = y+dy[i]
      if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy]==0:
        board[xx][yy]=1
        DFS(xx,yy)
        board[xx][yy]=0

board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
board[0][0] = 1
DFS(0, 0)
print(cnt)
