n = int(input())

g = []
for _ in range(n):
  a = list(map(int, input().split()))
  g.append(a)

start = end = n//2

def DFS(L, s):
  if L==n:
    print(s)
    return

  if L <= n//2:
    x = n//2 - L
    y = n//2 + L
  else:
    x = n//2 - (n-1-L)
    y = n//2 + (n-1-L)

  s += sum(g[L][x:y+1])
  
  DFS(L+1, s)

DFS(0,0)


############ SOLUTION #############
## BFS

from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
sum = 0
Q = deque()

ch[n//2][n//2] = 1
sum += a[n//2][n//2]
Q.append((n//2, n//2))
L = 0

while True:
  if L==n//2:
    break
  size = len(Q)     ## size만큼 for문이 돌아야함(좌표 수만큼 탐색)
  for i in range(size):
    tmp = Q.popleft()
    for j in range(4):
      x = tmp[0] + dx[j]
      y = tmp[1] + dy[j]
      if ch[x][y] == 0:
        sum += a[x][y]
        ch[x][y]=1
        Q.append((x,y))
  L += 1
  
print(sum)
