# Try 1 - 🔺
## 풀이 참고 보고 풀었다. 그리고 다 익지 않은 경우 처리에서 끼워맞춘 부분이 있다;

n, m = map(int, input().split())
t = [ list(map(int, input().split())) for _ in range(m) ]
dis = [[-100]*n for _ in range(m)]

from collections import deque
q = deque()
for i in range(m):
  for j in range(n):
    if t[i][j] == 1:
      dis[i][j]=0
      q.append((i, j))
    if t[i][j] == -1:
      dis[i][j] = -1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while q:
  x, y = q.popleft()
  for k in range(4):
    xx = x+dx[k]
    yy = y+dy[k]
    if 0<=xx<m and 0<=yy<n and t[xx][yy]==0:
      dis[xx][yy] = dis[x][y]+1
      t[xx][yy]=1
      q.append((xx, yy))

max_d = -2147000000
for i in range(m):
  for j in range(n):
    if dis[i][j]==-100:
      print(-1)
      exit()
    if dis[i][j]>max_d:
      max_d = dis[i][j]
print(max_d)
