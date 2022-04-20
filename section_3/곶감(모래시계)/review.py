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

#----------------------------------------------------#

# Try 2 - ✅
# 회전쓰 ~
# 행번호 방향(0-왼, 1-오) 격자수

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for _ in range(m):
  k, d, p = map(int, input().split())
  new_k = a[k-1].copy()
  p = p%n
  if d == 0:
    for i in range(n):
      a[k-1][i-p] = new_k[i]
  elif d == 1:
    for i in range(n):
      new_idx = i+p
      if new_idx >= n:
        new_idx -= n
      a[k-1][new_idx] = new_k[i]
      
s = 0
for i in range(n//2):
  s += sum(a[i][i:n-i])
  s += sum(a[n-i-1][i:n-i])

s += a[n//2][n//2]
print(s)

# 답은 맞았으나 모범답안이 훨씬 간단하다!! ㅜㅜ
