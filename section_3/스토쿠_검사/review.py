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

# Try 2 - ✅
m = [list(map(int, input().split())) for _ in range(9)]

# 행검사
for i in range(9):
  ch = [0]*10
  for j in range(9):
    number = m[i][j]
    ch[number] = 1
  if sum(ch)<9:
    print("NO")
    exit(0)
    

# 열검사
for i in range(9):
  ch = [0]*10
  for j in range(9):
    number = m[j][i]
    ch[number] = 1
  if sum(ch)<9:
    print("NO")
    exit(0)

# 사각형 검사
for i in range(3):
  for j in range(3):
    ch = [0]*10
    for k in range(i*3, (i+1)*3):
      for n in range(j*3, (j+1)*3):
        # print(k, n)
        number = m[k][n]
        ch[number] = 1
    if sum(ch)<9:
      print("NO")
      exit(0)
print("YES")

# 행, 열을 각각 돌지 않고, 답안에서처럼 한번 돌때 행, 열을 한번에 돌면서 중복 검사 하는 방법도 봐두자
