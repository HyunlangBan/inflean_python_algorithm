########### SOLUTION ##############
def DFS(L):
  global res
  if L==n:
    diff=max(money)-min(money)
    if diff<res:
      tmp = set()
      for x in money:
        tmp.add(x)
      if len(tmp)==3:
        res=diff
    
  else:
    for i in range(3):
      money[i]+=coin[L]
      DFS(L+1)
      money[i]-=coin[L]
      
n = int(input())
coin = []
money = [0]*3          ## 사람이 3명
res = 2147000000
for _ in range(n):
  coin.append(int(input()))
DFS(0)
print(res)
