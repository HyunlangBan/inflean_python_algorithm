# Try 1 - ✅
n = int(input())
a = []

for _ in range(n):
  h, w = map(int, input().split())
  a.append((w, h))

a.sort()
print(a)

# 본인보다 무거운 애들보다 키는 커야함
cnt = 1 # 가장 무거운 선수는 무조건 
for i in range(n-1):
  xh = a[i][1]
  for j in range(i+1, n):
    yh = a[j][1]
    if yh > xh:
      break
  else:
    print(a[i][0], a[i][1])
    cnt += 1

print(cnt)
