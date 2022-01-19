# 오른쪽, 아래로만 이동

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
t = [[2147000000]*n for _ in range(n)]
t[0][0] = m[0][0]

move = [(0, 1), (1, 0)]
def DFS(x, y):
  if x==n or y==n:
    return
  for a, b in move:
    xx=a+x
    yy=b+y
    if xx<n and yy<n:
      t[xx][yy]=min(t[xx][yy], t[x][y]+m[xx][yy])
      DFS(xx, yy)

DFS(0, 0)
print(t[-1][-1])

############ DFS로 풀었는데 시간이 너무 오래걸린다 -> 다이나믹으로 푸는게 더 효율적인 문제! #############
# dfs는 트리형태의 깊이 탐색을 하는데 그 깊이 즉 레벨값이 보통 20~25를 넘지 않아야 1초 타임 리밋을 피한다고 보통 생각합니다. 
# 뭐 적절히 컷에지를 하면 30정도까지도 해 볼 수 있구요.
# 하지만 50, 100 이런 깊이면 다이나믹이라 생각하면 됩니다.


############ SOLUTION - bottom up #############
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]

dy[0][0] = arr[0][0]
for i in range(n):
  dy[0][i] = dy[0][i-1]+arr[0][i]
  dy[i][0] = dy[i-1][0]+arr[i][0]

for i in range(1, n):
  for j in range(1, n):
    dy[i][j] = min(dy[i-1][j], dy[i][j-1])+arr[i][j]
print(dy[n-1][n-1])



############ SOLUTION 2 - top down #############
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]     ## memoization

def DFS(x, y):
  if dy[x][y] > 0:
    return dy[x][y]
  if x==0 and y==0:
    return arr[0][0]
  else:
    if y==0:
      dy[x][y] = DFS(x-1, y)+arr[x][y]
    elif x==0:
      dy[x][y] = DFS(x, y-1)+arr[x][y]
    else:
      dy[x][y] = min(DFS(x-1, y), DFS(x, y-1))+arr[x][y]
    return dy[x][y]
    
print(DFS(n-1, n-1))
