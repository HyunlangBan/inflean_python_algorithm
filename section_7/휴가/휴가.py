n = int(input())
a = []
for _ in range(n):
  t, p = map(int, input().split())
  a.append((t, p))

def DFS(L, idx, t, p):
  global res
  if t == n:
    if p > res:
      res = p
    return

  for i in range(idx, n):
    t += a[i][0]
    p += a[i][1]
    next = i + a[i][0]
    DFS(L+1, next, t, p)
    t -= a[i][0]
    p -= a[i][1]

res = -2174000000
DFS(0, 0, 0, 0)
print(res)

############# SOLUTION ##############
## 부분집합
## L: 인덱스 겸 누적 일수

def DFS(L, sum):
  global res
  if L==n+1:
    if sum > res:
      res = sum
    else:
      if L+T[L] <= n+1:   # 날짜에 잡힌 상담을 진행
        DFS(L+T[L], sum+P[L])
      DFS(L+1, sum)

n = int(input())
T = list()
P = list()
for i in range(n):
  a, b = map(int, input().split())
  T.append(a)
  P.append(b)
res = -2147000000
T.insert(0, 0)      ## idx를 날짜와 맞추기 위하여(1일부터 시작)
P.insert(0, 0)
DFS(1, 0)
print(res)
