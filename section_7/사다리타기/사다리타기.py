board = []
move = [(-1, 0), (0, -1), (0, 1)]
visited = [[0]*10 for _ in range(10)]

for _ in range(10):
  board.append(list(map(int, input().split())))

def DFS(i, j):
  visited[i][j]=1
  if i == 0:
    print(j)
  else:
    for m_x, m_y in move:
      xx = i + m_x
      yy = j + m_y
      if 0<=xx<10 and 0<yy<10 and board[xx][yy]==1 and not visited[xx][yy]:
        DFS(xx, yy)

for i in range(10):
  for j in range(10):
    if board[i][j]==2:
      DFS(i, j)
      
## 사다리타기라는 것을 고려하지 않았음..!


############# SOLUTION ###############
## 사다리를 역으로 탸기 -> 왼쪽, 오른쪽 갈 수 없으면 위로
def DFS(x, y):
  ch[x][y]=1
  if x==0:
    print(y)
  else:  ## 왼쪽, 오른쪽, 위 순으로 우선순위
    if y-1>=0 and board[x][y-1]==1 and ch[x][y-1]==0:
      DFS(x, y-1)
    elif y+1<10 and board[x][y+1]==1 and ch[x][y+1]==0:
      DFS(x, y+1)
    else:
      DFS(x-1, y)

board = [list(map(int, input().split())) for _ in range(10)]
ch = [[0]*10 for _ in range(10)]
for y in range(10):
  if board[9][y]==2:   ### 어차피 2는 맨 마지막 행에 있을 것이므로 마지막 행만 탐색
    DFS(9, y)
