# 안전한 영역 - 위, 아래, 오, 왼 인접하여 물에 잠기지 않음
# 장마철 물에 잠기지 않는 안전 영역의 최대 개수

n = int(input())
board = [ list(map(int, input().split())) for _ in range(n) ]

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

from collections import deque
max_cnt = -2147000000

for h in range(100):
  ch = [[0]*n for _ in range(n)]
  cnt = 0
  q = deque()
  for i in range(n):
    for j in range(n):
      if ch[i][j]==0 and board[i][j] > h:
        cnt += 1
        q.append((i, j))
        ch[i][j]=1

        while q:
          x, y = q.popleft()
          for a, b in move:
            xx = a + x
            yy = b + y
            if 0<=xx<n and 0<=yy<n and board[xx][yy]>h and ch[xx][yy]==0:
              q.append((xx, yy))
              ch[xx][yy]=1

  max_cnt = max(cnt, max_cnt)
  
  if cnt == 0:
    break

print(max_cnt)
