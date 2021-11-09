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
  

############### SOLUTION ################# 

def DFS(L, s):
  global cnt
  if L==m:
    for j in range(L):
      print(res[j], end=' ')
    cnt += 1
    print()
  else:
    for i in range(s, n+1):
      res[L] = i
      DFS(L+1, i+i)
  
  
res = [0] * (n+1)
cnt = 0
DFS(0, 1)
print(cnt)
