# Try 1 - ✅

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

# 최대한 꽉 채워서 보내기
cnt = 0
while a:
  print(a)
  big = a.pop(0)
  for i in range(len(a)):
    if a[i] <= m-big:
      a.pop(i)
      break
  cnt += 1

print(cnt)

# Try 2 - ✅
n, m = map(int, input().split())
a = list(map(int, input().split()))

# 한번 보낼때 최대한 두명으로 맞춰서 보내기
a.sort(reverse=True)

cnt = 0
while a:
  print(a)
  p = a.pop(0)
  cnt += 1
  for i in range(len(a)):
    if p + a[i] <= m:
      a.remove(a[i])
      break

print(cnt)
