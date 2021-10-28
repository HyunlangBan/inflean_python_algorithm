from collections import deque

prereq = list(input())

n = int(input())
for _ in range(n):
  q = deque(prereq)
  plan = input()
  for i in plan:
    if q:
      if i == q[0]:
        q.popleft()
        if not q:
          print("YES")
          break
    else:
      print("YES")
      break
  else:
    print("NO")
    
## 이거보다 깔끔한 방법이 있을 것 같은 느낌....
