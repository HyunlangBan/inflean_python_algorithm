# Try 1 - ❌

# 1: 벽
# 0: 통로
m = [list(map(int, input().split())) for _ in range(7)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0

def DFS(x, y):
  global cnt
  if x==6 and y==6:
    cnt += 1
    return

  for i in range(4):
    xx = x+dx[i]
    yy = y+dy[i]
    if 0<=xx<7 and 0<=yy<7 and m[xx][yy] == 0:
      m[xx][yy]=1
      DFS(xx, yy)
      m[xx][yy]=0 ######### 빠진 부분

m[0][0]=1
DFS(0, 0)

print(cnt)
