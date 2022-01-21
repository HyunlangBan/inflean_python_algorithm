############ SOLUTION ################

n = int(input())
coin = list(map(int, input().split()))
m = int(input())
dy = [1000] * (m+1)
dy[0] = 0    ## 주의! 빼먹으면 안된다.

for i in range(n):
  for j in range(coin[i], m+1):
    dy[j] = min(dy[j], dy[j-coin[i]]+1)
print(dy[m])
