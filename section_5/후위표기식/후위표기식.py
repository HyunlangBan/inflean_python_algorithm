a = list(input())

stack = [a[0]]
priority = False
for i in range(1, len(a),2):
  if a[i] in ['*', '/'] or priority:
    if a[i+1] =='(':
      stack.append(a[i])
      priority = True
    if stack[-1] in ['-', '+'] or priority:
      p = stack.pop()
      stack.append(a[i+1])
      stack.append(a[i])
      stack.append(p)
  elif a[i] in ['-', '+']:
    stack.append(a[i+1])
    stack.append(a[i])
  else:
    if a[i] == ')':
      pritority = False
    else:
      stack.append(a[i])

print(stack)

## stack -> 연산 중에서 부호를 가장 뒤로 저장하고 추가될 부호와 비교하여 우선순위가 낮으면 뒤로 추가하고 높으면 이전 부호 앞으로 

######## 포기... 노력했다....
################ SOLUTION ################
## 후위표기식 -> 컴퓨터가 순차 처리 가능 (부호를 만나면 그 앞의 두개의 수를 연산한다.)
## 숫자는 print하고 부호는 stack에 쌓는다.
## 같은 우선순위의 부호는 순서대로 처리한다.
## 현재 부호와 stack의 최상단 부호를 비교 => 최상단 부호가 현재 부호의 우선순위와 동일하거나 높다면 pop하고 아니면 현재 부호를 쌓는다.
## +나 -(부호 우선순위 최하)가 나오면 stack에 있는 부호들을 모두 꺼내준다.

a = input()
stack = []
res = ''

for x in a:
  if x.isdecimal():
    res += x
  else:
    if x=='(':
      stack.append(x)
    elif x=='*' or x == '/':
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        res += stack.pop()
      stack.append(x)
    elif x=='+' or x == '-': # stack에 있는 모든 것을 끄집어냄
      while stack and stack[-1] != '(':
        res += stack.pop()
      stack.append(x)
    elif x == ')':
      while stack and stack[-1] != '(':
        res += stack.pop()
      stack.pop()
      
while stack:
  res += stack.pop()
  
print(res)
      
