from collections import deque

g = []
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(7):
  a = list(map(int, input().split()))
  g.append(a)

visited = [[0]*7 for _ in range(7)]
cnt = [[0]*7 for _ in range(7)]
q = deque([(0, 0)])

res = []
while q:
  x, y = q.popleft()
  if x==6 and y==6:
    res.append(cnt[x][y])
  visited[x][y] = 1
  for a, b in move:
    next_x = x+a
    next_y = y+b
    if 0<=next_x<7 and 0<=next_y<7:
      if g[next_x][next_y] == 0:
          if visited[next_x][next_y] == 1:
            if cnt[next_x][next_y] > cnt[x][y]+1:
             cnt[next_x][next_y] = cnt[x][y]+1
          else:
            cnt[next_x][next_y] = cnt[x][y]+1
            q.append((next_x, next_y))
  
if res==[]:
  print(-1)
else:
  print(min(res))

  
########### SOLUTION ############
## 더깔끔 - visited, cnt를 한번에 해결

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = [list(map(int, input().split())) for _ in range(7)]
dis = [[0] * 7 for _ in range(7)]
Q = deque()
Q.append((0, 0))
board[0][0] = 1  ## 1로 바꾸면 더이상 방문하지 않는다.
while Q:
  tmp = Q.popleft()
  for i in range(4):
    x = tmp[0] + dx[i]
    y = tmp[1] + dy[i]
    if 0<=x<=6 and 0<=y<=6 and board[x][y]==0:
      board[x][y]=1
      dis[x][y]=dis[tmp[0]][tmp[1]]+1
      Q.append((x,y))
if dis[6][6]==0:
  print(-1)
else:
  print(dis[6][6])
