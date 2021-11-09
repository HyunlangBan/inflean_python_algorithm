n, m = map(int, input().split())
a = [0] * n

def DFS(L):
  global cnt
  if L==n:
    if sum(a)==2:
      cnt += 1
      for i in range(n):
        if a[i] == 1:
          print(i+1, end=' ')
      print()
    return

  a[L] = 1
  DFS(L+1)
  a[L] = 0
  DFS(L+1)
  
cnt = 0
DFS(0)
print(cnt)
  
