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


# Try 2 - ❌

n, c = map(int, input().split())
a = []
for _ in range(n):
  a.append(int(input()))

a.sort()

print(a)

## 최대거리
lt = 1
rt = a[-1]

def count(dist):
  p = 0
  cnt = 1
  
  # 말은 next보다 같거나 큰 마구간으로 가야한다.
  for i in range(n):
    next = a[p] + dist
    print(next)
    if a[i] == next:
      p = i
      cnt += 1
    elif a[i] > next:
      p = i+1
      cnt += 1

  return cnt

result = -2147000000
while lt<=rt:
  mid = (lt+rt)//2
  print(f'mid: {mid}')
  if count(mid) <= c:
    result = mid
    rt = mid - 1
  else:
    lt = mid + 1

print(result)

# count 어떻게 해야하는지 모르겠음
# while 내에서 분기하는거 자꾸 틀림 
