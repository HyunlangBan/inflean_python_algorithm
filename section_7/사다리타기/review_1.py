# 사다리는 1로 표현
# 도착지점은 2로 표현

# 사다리는 우선순위가 있음
# 좌우 중 먼저 나오는 것 그 다음 위

board = [ list(map(int, input().split())) for _ in range(10) ]

for i in range(10):
  if board[-1][i] == 2:
    start = i
    break

move = [(0, -1), (0, 1), (-1, 0)]

def DFS(x, y):
  # print(f'x,y = {x}, {y}')
  if x == 0:
    print(y)
    return

  for a, b in move:
    xx = x+a
    yy = y+b
    if 0<=xx<10 and 0<=yy<10 and board[xx][yy]==1:
      board[xx][yy]=0
      DFS(xx, yy)
      break

board[9][start]=0
DFS(9, start)
