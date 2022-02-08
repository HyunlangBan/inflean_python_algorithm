# Try 1 - ✅

a = [ list(map(int, input().split())) for _ in range(9) ]

for i in range(9):
  visited = [0]*10
  for j in range(9):
    number = a[i][j]
    if visited[number]:
      print("NO")
      exit()
    visited[number] = 1

for i in range(9):
  visited = [0]*10
  for j in range(9):
    number = a[j][i]
    if visited[number]:
      print("NO")
      exit()
    visited[number] = 1

for i in range(3):
  for j in range(3):
    visited = [0]*10
    for k in range(i*3, (i+1)*3):
      for m in range(j*3, (j+1)*3):
        number = a[k][m]
        if visited[number]:
          print("NO")
          exit()
        visited[number]=1
    print(visited)

print("YES")
