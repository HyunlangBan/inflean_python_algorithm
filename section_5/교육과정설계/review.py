## Try 1 - ✅
order = list(input())
n = int(input())

for _ in range(n):
    stack = []
    courses = input()
    for c in courses:
        if c in order and c not in stack:
            stack.append(c)
    if stack == order:
        print("YES")
    else:
        print("NO")


# Try 2 - ✅
req = input()
n = int(input())

res = []

for _ in range(n):
  c = input()
  y = list(req)
  for x in c:
    if y and x == y[0]:
      y.pop(0)

    if not y:
      res.append("YES")
      break
  else:
    res.append("NO")

for i, s in enumerate(res, 1):
  print(f'#{i} {s}')
