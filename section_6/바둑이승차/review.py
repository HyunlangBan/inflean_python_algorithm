# Try 1 - β
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

# Try 2 - πΊ
c, n = map(int, input().split())
a = [int(input()) for _ in range(n)]

### κ°μ₯ λ¬΄κ±°μ΄ λΆλΆ μ§ν©μ κ΅¬νκΈ° 
res = 0
total = sum(a)

def DFS(L, s):
  global res
  
  # cut-edge
  if s + (total-s) <= res:
    ## λ¨μν total - sλ‘ νλ©΄ μλ¨! μ νμ μνκΈ°λ‘ μ νν μ λ€μ΄ ν¬ν¨μ΄ μλμ΄ μμΌλ―λ‘
    ## λ΅μ μ°Έμ‘°ν κ²    
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
