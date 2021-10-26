a = list(input()). ## string이므로 list가 필요 없음
tmp = []
res = 0

for i in a:
  if i not in ['+', '-', '*', '/']: ## i.isdecimal()
    tmp.append(i)
  else:
    x = tmp.pop()
    y = tmp.pop()
    cal = eval(y+i+x)
    tmp.append(str(cal))
    res = cal

print(res)  ## print(tmp[0])
