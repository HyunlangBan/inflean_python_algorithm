# Try 1 - ✅
# 위, 아래, 왼, 오 중 더 높은 구역으로만 이동 가능 
# 출발지는 가장 낮은 곳
# 목적지는 가장 높은 곳

highest = -2147000000
lowest = 2147000000
sx = 0
sy = 0
ex = 0
ey = 0

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]

for i in range(n):
  for j in range(n):
    if g[i][j] < lowest:
      lowest = g[i][j]
      sx = i
      sy = j
    if g[i][j] > highest:
      highest = g[i][j]
      ex = i
      ey = j

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = 0

# 등산경로는 몇가지?
def DFS(x, y):
  global cnt
  if x==ex and y==ey:
    cnt += 1
    return
  for k in range(4):
    xx = x+dx[k]
    yy = y+dy[k]
    if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and g[x][y]<g[xx][yy]:
      # height = g[xx][yy]
      # g[xx][yy]=-1         ## 이렇게 바꿔두면 나중에 높이 비교할때 문제가 생기므로 ch에서 따로 체크해주어야 함!
      ch[xx][yy]=1
      DFS(xx, yy)
      ch[xx][yy]=0

ch[sx][sy] = 1
DFS(sx, sy)
print(cnt)
