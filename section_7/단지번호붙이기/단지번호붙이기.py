################## SOLUTION - DFS ####################

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
  global cnt
  cnt += 1
  board[x][y] = 0
  for i in range(4):
    xx = x+dx[i]
    yy = y+dy[i]
    if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
      DFS(xx, yy)
  
n = int(input())
board = [list(map(int, input())) for _ in range(n)]
res = []

for i in range(n):
  for j in range(n):
    if board[i][j]==1:
      cnt = 0
      DFS(i, j)
      res.append(cnt)
     
print(len(res))
res.sort()
for x in res:
  print(x)
  
  
################ SOLUTION - BFS ##################

from collections import deque
sys.stdin=open("input.txt", "r")
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
board=[list(map(int, input())) for _ in range(n)]
cnt=0
res=[]
Q=deque()
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=0
            Q.append((i, j))
            cnt=1
            while Q:
                tmp=Q.popleft()
                for k in range(4):
                    x=tmp[0]+dx[k]
                    y=tmp[1]+dy[k]
                    if x<0 or x>=n or y<0 or y>=n or board[x][y]==0:
                        continue
                    board[x][y]=0
                    Q.append((x, y))
                    cnt+=1
            res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)
