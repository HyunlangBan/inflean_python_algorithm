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

############## SOLUTION ################
## 수업 계획에서 필수과목인지 아닌지 확인해야함

need = input()
n = int(input())

for i in range(n):
  plan = input()
  dq = deque(need)
  
  for x in plan:
    if x in dq:
      if x != dq.popleft():
        print("NO")
        break
  else:
    if len(dq)==0:
      print("YES")
    else:
      print("NO")
