############## SOLUTION #################
## 트리가 n가닥으로 뻗음
def DFS(L):
  global cnt
  if L == m:
    for i in range(m):
      print(res[j], end=' ')
    print()
    cnt += 1
    
  else:
    for i in range(1, n+1):
      res[L] = i
      DFS(L+1)

n, m = map(int, input().split())
res = [0] * m
cnt = 0
DFS(0)
print(cnt)
