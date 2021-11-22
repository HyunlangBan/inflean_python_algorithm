n, m = map(int, input().split())

# n개의 문제 중 최대 점수를 얻을 수 있도록
# 조합
a = []
for _ in range(n):
  s, t = map(int, input().split())
  a.append((s, t))

def DFS(L, idx, s, t):
  global res
  if t == m:
    if s > res:
      res = s
    return
  elif t < m:
    if s > res:
      res = s

  for i in range(idx, n):
    t += a[i][1]
    s += a[i][0]
    DFS(L+1, i+1, s, t)
    t -= a[idx][1]
    s -= a[idx][0]

res = -2147000000
DFS(0, 0, 0, 0)
print(res)

############# SOLUTION ###############
## 부분집합
## DFS(L, 시간, 총점)
def DFS(L, sum, time):
  global res
  if time > m:
    return
  if L==n:
    if sum > res:
      res = sum
  else:
    DFS(L+1, sum+pv[L], time+pt[L])
    DFS(L+1, sum, time)
    
n, m = map(int, input().split())
pv = list()
pt = list()

for i in range(n):
  a, b = map(int, input().split())
  pv.append(a)
  pt.append(b)
res = -2147000000
DFS(0, 0, 0)
