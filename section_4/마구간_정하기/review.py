# Try 1 - ๐บ

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


# Try 2 - โ

n, c = map(int, input().split())
a = []
for _ in range(n):
  a.append(int(input()))

a.sort()

print(a)

## ์ต๋๊ฑฐ๋ฆฌ
lt = 1
rt = a[-1]

def count(dist):
  p = 0
  cnt = 1
  
  # ๋ง์ next๋ณด๋ค ๊ฐ๊ฑฐ๋ ํฐ ๋ง๊ตฌ๊ฐ์ผ๋ก ๊ฐ์ผํ๋ค.
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

# count ์ด๋ป๊ฒ ํด์ผํ๋์ง ๋ชจ๋ฅด๊ฒ ์
# while ๋ด์์ ๋ถ๊ธฐํ๋๊ฑฐ ์๊พธ ํ๋ฆผ 
