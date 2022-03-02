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
