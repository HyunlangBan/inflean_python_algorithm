# Try 1 - ❌

n = int(input())
time_table = []
for _ in range(n):
  t, p = map(int, input().split())
  time_table.append((t,p))

res = -2147000000
def DFS(idx, sum):
  global res
  if idx >= n:                   ####### idx == n
    res = max(res, sum)
    return

  if idx+time_table[idx][0] < n: ###### idx+time_table[idx][0] <= n
    DFS(idx+time_table[idx][0], sum+time_table[idx][1])
  else:         ###### else 삭제
    DFS(idx+1, sum)      ###### if절 바깥이어야 함
    
DFS(0, 0)
print(res)
