# Try1 - ✅
n, m = map(int, input().split())
# n번까지의 구슬 중 m개를 뽑아 일열로 나열하는 경우의 수

res = [0]*m
check = [0]*n

def DFS(L):
  if L==m:
    print(res)
    return
  for i in range(n):
    if check[i] == 0:
      check[i]=1
      res[L] = i+1
      DFS(L+1)
      check[i]=0

DFS(0)
