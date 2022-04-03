# Try 1 - ❌

from collections import deque

s, e = map(int, input().split())
q = deque([s])
cnt = [0]*10001
v = [0]*10001
v[s]=1
while q:
  cur = q.popleft()
  if cur == e:
    print(cnt[cur])
    break
  for i in [5, 1, -1]:
    ###### 조건이 더 필요하다!!!  => if 0<cur+i<=10000
    if not v[cur+i]:
      v[cur+i]=1
      q.append(cur + i)
      cnt[cur + i] = cnt[cur] + 1
