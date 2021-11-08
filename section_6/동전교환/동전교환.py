###### 으아아아ㅏ 모르겠다

n = int(input())
a = list(map(int, input().split()))
m = int(input())

def DFS(idx, money):
  global cnt

  if money >= a[idx]:
    money -= a[idx]
    cnt += 1
    if money==0:
      print(cnt)
      cnt = 0
  else:
    return

  if idx >= n-1:
    return

  print(money)
  DFS(idx+1, money)

cnt = 0
DFS(0, m)

############## SOLUTION ################
## 중복순열과 유사한 풀이

dfs DFS(L, sum):
  global res
  
  if L > res:   ## Cut Edge
    return
  if sum > m:
    return
  if sum == m:
    if L < res:
      res = L
      
  else:
    for i in range(n):
      DFS(L+1, sum + a[i])
      
      
res = 2147000000
a.sort(reverse=True)
DFS(0, 0)
print(res)
