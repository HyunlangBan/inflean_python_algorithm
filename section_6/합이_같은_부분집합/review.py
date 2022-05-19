# Try - ❌
## cut-edge도 맞았는데 for문 쓰면 안됐음!!! ㅠㅠ

n = int(input())
a = list(map(int, input().split()))
total = sum(a)
s = 0
def DFS(L, s):
  ## cut-edge

  if s > total//2:
    return
  if L == n:
    if s == total-s:
      print("YES")
      exit(0)

  for i in range(L, n):
    DFS(L+1, s+a[i])
    DFS(L+1, s)

DFS(0, 0)
print("NO")
