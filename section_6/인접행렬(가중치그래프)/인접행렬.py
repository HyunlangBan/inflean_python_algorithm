n, m = map(int, input().split())

matrix = [[0]*n for _ in range(n)]

for _ in range(m):
  x, y, w = map(int, input().split())

  matrix[x-1][y-1]=w

for i in range(n):
  for j in range(n):
    print(matrix[i][j], end = ' ')
  print()
