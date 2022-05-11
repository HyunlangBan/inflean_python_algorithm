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

# Try 2 - ✅
n = int(input())
a = list(map(int, input().split()))

# 양 끝의 수들 중에 작은 값을 가져온다.
from collections import deque
q = deque(a)
x = -1
res = ''
while q:
  l = q[0]
  r = q[-1]
  
  if x != -1 and x>l and x>r:
    break
  
  if l>x and r>x:
    if l<r:
      res += 'L'
      q.popleft()
      x = l
    else:
      res += 'R'
      q.pop()
      x = r
      
  elif l>x and r<x:
    res += 'L'
    q.popleft()
    x = l
  elif r>x and l<x:
    res += 'R'
    q.pop()
    x = r
    
print(len(res))
print(res)

# 어떤 경우로 나눠야할지 생각하는게 좀 어려웠다.
