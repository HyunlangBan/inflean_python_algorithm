# Try 1 - 🔺
## 어이없는 걸로 틀림 !!!!!! ㅠㅠㅠ
## 답지에서는 ch말고 방문한 곳을 0으로 바꾸어서 했는데 그게 더 깔끔하고 좋은 것 같다.

from collections import deque

n = int(input())
a = []
ch = [[0]*n for _ in range(n)]
for _ in range(n):
  a.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

g_cnt = 0
apt_cnts = []
for i in range(n):
  for j in range(n):
    if a[i][j]==1 and ch[i][j]==0:
      g_cnt += 1
      
      # BFS START
      q = deque([(i,j)])
      apt_cnt = 1
      ch[i][j] = 1
      while q:
        
        cx, cy = q.popleft()
        for i in range(4):       ##### 위에서 i를 쓰고 있는데 i로 썼다....다른 변수를 이용하자
          xx = cx + dx[i]
          yy = cy + dy[i]
          if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and a[xx][yy]==1:
            ch[xx][yy]=1
            q.append((xx,yy))
            apt_cnt += 1
      apt_cnts.append(apt_cnt)

print(g_cnt)
apt_cnts.sort()
for i in range(g_cnt):
  print(apt_cnts[i])
  
  
