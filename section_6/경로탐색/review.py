# Try - 1 ❌
# 중복 체크를 그래프로 했는데, 방문한 노드만 다시 방문하지 않으면 되므로 리스트로 해야한다.

n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
  x, y = map(int, input().split())
  graph[x][y] = 1

ch = [[0]*(n+1) for _ in range(n+1)]
ch = [0]*(n+1)
cnt = 0

print(graph)
def DFS(point):
  global cnt
  if point == n:
    cnt += 1
    return

  for i in range(1, n+1):
    if graph[point][i] == 1 and ch[point][i]==0:
      ch[point][i]=1
      DFS(i)
      ch[point][i]=0
    
DFS(1)
print(cnt)
  
