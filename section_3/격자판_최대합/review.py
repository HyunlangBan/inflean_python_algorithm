## Try 1

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

sum = 0
for i in range(n):
  x_sum = 0
  y_sum = 0
  for j in range(n):
    x_sum += a[i][j]
    y_sum += a[j][i]
  sum = max(x_sum, y_sum, sum)

a_sum = 0
b_sum = 0
for i in range(n):
  a_sum += a[i][i]
  b_sum += a[i][n-i-1]
sum = max(sum, a_sum, b_sum)

print(sum)
