# Try 1 - ✅

n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
ch = [0]*n

cnt = 0
def DFS(L, idx, sum):
  global cnt
  if L==k:
    if sum%m==0:
      cnt += 1
    return

  for i in range(idx, n):
    if ch[i]==0:
      ch[i]=1
      DFS(L+1, i, sum+a[i])
      ch[i]=0

DFS(0, 0, 0)
print(cnt)
