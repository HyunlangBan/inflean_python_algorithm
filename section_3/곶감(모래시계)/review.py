# Try 1 - ❌

import copy

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
aa = copy.deepcopy(a)
m = int(input())

for _ in range(m):
  x, y, z = map(int, input().split())
  if y==0:
    # 왼쪽
    for i in range(n):
      if i-z<0:
        move = i-z+n
      else:
        move = i-z
      print(f'move={move}')
      aa[x-1][move] = a[x-1][i]
  else:
    # 오른쪽
    for i in range(n):
      if i+z>=n:
        move = i+z-n
      else:
        move = i+z
      print(f'move={move}')
      aa[x-1][move] = a[x-1][i]

result = 0
for i in range(n//2):
  s, e = i, n-i
  r1 = aa[i]
  r2 = aa[n-i-1]
  result += sum(r1[s:e])
  result += sum(r2[s:e])
result += aa[n//2][n//2]

print(result)

## 회전을 한바퀴 이상 하는 경우를 생각하지 못해서 오답 발생
