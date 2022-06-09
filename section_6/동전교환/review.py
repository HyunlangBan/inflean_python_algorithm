# Review - ❌
n = int(input())
coins = list(map(int, input().split()))
m = int(input()) # 거슬러줄 금액

coins.sort(reverse=True)
res = 0

def DFS(money):
  global cnt
  if money == 0:
    print(cnt)
    exit()
    return

  for i in range(n):
    if money % coins[i]==0:
      cnt += 1
      money -= coins[i]
      DFS(money)

DFS(m)
