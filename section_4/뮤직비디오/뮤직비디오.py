n, m = map(int, input().split())
t =list(map(int, input().split()))

lt = 1
longest = sum(t)
rt = longest
res = 0

def count(mid):
  total = 0
  cnt = 0
  for i in t:
    if total+i > mid:
      cnt += 1
      total = 0
    total += i
  if total > 0:
    cnt += 1
  return cnt

while lt<=rt:
  mid = (lt+rt)//2
  if count(mid) <= 3:
    res = mid
    rt -= 1
  if count(mid) > 3:
    lt += 1

print(res)
