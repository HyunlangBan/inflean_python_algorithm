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
