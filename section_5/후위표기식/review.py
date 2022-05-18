# Try - ❌
## 어려워...........

from collections import deque
a = input()

stack = []
q = deque(a)
op = []

while q:
  print(op)
  print(stack)
  x = q.popleft()
  if x.isdigit():
    stack.append(x)
    if op:
      if op[-1] == '*' or op[-1] == '/':
        stack.append(op.pop())
  else:
      if x == ')':
        while True:
          l = op.pop()
          print(l)
          if l == '(':
            break
          else:
            stack.append(l)
      else:
          op.append(x)

while op:
  stack.append(op.pop())
      
    
print(stack)

# 첫번째 예제만 끼워 맞춤...
