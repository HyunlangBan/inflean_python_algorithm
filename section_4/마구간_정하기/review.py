# Try 1 - 🔺

n, c = map(int, input().split())
a = []

for _ in range(n):
  x = int(input())
  a.append(x)

a.sort()

lt = 1
rt = a[-1]-a[0]

def count(dist):
  cnt = 1
  s = a[0]
  for i in a:
    if s+dist <= i:
      cnt += 1
      s = i
  return cnt

result = -1
while lt <= rt:
  mid = (lt+rt)//2
  cnt = count(mid)
  if cnt >= c:
#     if cnt == c:
    result = max(result, mid)
    lt = mid+1
  else:
    rt = mid-1
  
print(result)
