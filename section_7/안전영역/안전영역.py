################# SOLUTION - BFS #####################
## 방문했다고 지도 원본을 수정하면 안된다 ! ! (체크 배열을 따로 만들어야한다.) -> 이후에도 다른 높이 기준으로 방문할 것이므로
sys.setrecursionlimit(10**6) ## recursion timelimit 설정

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y , h):
  ch[x][y] = 1
  for i in range(4):
    xx = x+dx[i]
    yy = y+dy[i]
    if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>h:
      DFS(xx, yy, h)
      

n = int(input())
cnt = 0
res = 0
board = [list(map(int, input().split())) for _ in range(n)]
for h in range(100):
  ch = [[0]*n for _ in range(n)] ## 높이가 변할때마다 check list는 초기화된다.
  cnt = 0
  for i in range(n):
    for j in range(n):
      if ch[i][j] == 0 and board[i][j] > h:
        cnt += 1 ## 안전영역
        DFS(i, j, h)
  res = max(res, cnt)
  if cnt == 0:  ## 현재 높이가 최대 높이보다 커졌을때
    break

print(res)
 
