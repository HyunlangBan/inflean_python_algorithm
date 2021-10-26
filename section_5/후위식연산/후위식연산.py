a = list(input())
tmp = []
res = 0

for i in a:
  if i not in ['+', '-', '*', '/']:
    tmp.append(i)
  else:
    x = tmp.pop()
    y = tmp.pop()
    cal = eval(y+i+x)
    tmp.append(str(cal))
    res = cal

print(res)
