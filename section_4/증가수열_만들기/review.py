# Try 1 - ❌

n = int(input())
a = list(map(int, input().split()))
from collections import deque
a = deque(a)

l = deque()
r = deque()

if a[0] < a[-1]:
  p = a.popleft()
  print("L")
else:
  p = a.pop()
  print("R")

while True:
  l.append(a.popleft())
  r.append(a.pop())

  if p < l[0] and p < r[0]:
    if l[0] < r[0]:
      print("L")
      p = l.popleft()
    else:
      print("R")
      p = r.pop()
  elif p < l[0]:
      print("L")
      p = l.popleft()
  elif p < r[0]:
      print("R")
      p = r.pop()
  else:
    break
    
## 적절한 해결 방법이 떠오르지 않았음 ㅜ
