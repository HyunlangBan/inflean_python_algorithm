# Try - 1 ✅

n, m = map(int, input().split())
a = list(map(int, input().split()))

min = 1
max = 10000000

def count(size):
  cnt = 1
  sum = 0
  for i in a:
    sum += i
    if sum > size:
      cnt += 1
      sum = i
  return cnt
    
  
min_size = 10000000
while min<=max:
  mid = (min+max)//2
  cnt = count(mid)
  # print(min, max)
  if cnt <= m:
    min_size = mid
    max = mid-1
  else:
    min = mid+1
    
print(min_size)

# max를 하드코딩 하지 말고 sum(a)로 하자  

# Try 2 - ✅

n, m = map(int, input().split())

a = list(map(int, input().split()))

# 3개의 DVD에 9개의 DVD를 넣고, DVD 하나당 길이는 최소가 되게 하라.

s = 1 ## 0은 최소값이 될 수 없음
e = sum(a)
def check(t):
  cnt = 1 
  add = 0
  for i in a:
    add += i
    if add > t:
      cnt += 1
      add = i
  return cnt

result = 2147000000
while s <= e: ## 같아질때까지 돌기
  mid = (s+e)//2
  cnt = check(mid)
  print(s, e, mid, cnt)
  if cnt > m:
    s = mid + 1
  else:
    result = min(mid, result)
    e = mid - 1
    
print(result)

# while 안에서 분기를 탈때 cnt>m이 아니라 cnt<=m일때를 먼저 하면 min을 쓰지 않아도 최소값이 될떄까지만 result가 갱신된다. 
# 노래를 쪼개서 담을 수 없으므로 DVD 하나의 길이는 노래 한곡의 최대 길이보다 길어야한다. (조건 추가 필요)
