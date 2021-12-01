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
