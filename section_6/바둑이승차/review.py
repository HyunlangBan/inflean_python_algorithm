# Try 1 - ❌
c, n = map(int, input().split())
dogs = []

for _ in range(n):
  dogs.append(int(input()))

m_sum = 0
def DFS(idx, sum):
  global m_sum
  if idx == n:
    print(m_sum)
    return
  if sum > c:
    return
  elif sum <= c:
    m_sum = max(m_sum, sum)
    
  DFS(idx+1, sum+dogs[idx])
  DFS(idx+1, sum)

DFS(0, 0)

# Try 2 - 🔺
c, n = map(int, input().split())
a = [int(input()) for _ in range(n)]

### 가장 무거운 부분 집합을 구하기 
res = 0
total = sum(a)

def DFS(L, s):
  global res
  
  # cut-edge
  if s + (total-s) <= res:
    ## 단순히 total - s로 하면 안됨! 선택을 안하기로 선택한 애들이 포함이 안되어 있으므로
    ## 답안 참조할것    
    return
  if s > c:
    return
  if L==n:
    if s > res:
      res = s
    return

  DFS(L+1, s+a[L])
  DFS(L+1, s)

DFS(0, 0)
print(res)
