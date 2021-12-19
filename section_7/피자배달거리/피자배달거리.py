############### SOLUTION ###################

def DFS(L, s):
  global res
  if L==m:
    sum = 0 ## 모든 도시의 총 피자 배달 거리
    for j in range(len(hs)):
      x1 = hs[j][0]
      y1 = hs[j][1]
      dis = 2147000000
      for x in cb:
        x2 = pz[x][0]
        y2 = pz[x][1]
        dis = min(dis, abs(x1-x2)+abs(y1-y2))
      sum+=dis
    if sum<res:
      res=sum
      
  else:
    for i in range(s, len(pz)):
      cb[L]=i
      DFS(L+1, i+1)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

## 집과 피자집의 좌표 정보를 각각 저장한다.
hs = []
pz = []
cb = [0]*m       ## 살아남을 피자집들
res = 2147000000

for i in range(n):
  for j in range(n):
    if board[i][j]==1:
      hs.append((i, j))
    elif board[i][j]==2:
      pz.append((i, j))
DFS(0, 0)
print(res)
