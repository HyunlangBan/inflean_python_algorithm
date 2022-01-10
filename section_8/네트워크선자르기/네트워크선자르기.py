############### SOLUTION - Botton up #################


n = int(input())
dy = [0] * (n+1)

# 직관적으로 알 수 있는것은 직접 표기
dy[1] = 1
dy[2] = 2

for i in range(3, n+1):
  dy[i] = dy[i-1]+dy[i-2]

print(dy[n])


################ SOLUTION - Top down ##################
### 재귀, 메모이제이션

