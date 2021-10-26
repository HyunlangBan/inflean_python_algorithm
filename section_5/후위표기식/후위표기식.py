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
