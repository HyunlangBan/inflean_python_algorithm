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
