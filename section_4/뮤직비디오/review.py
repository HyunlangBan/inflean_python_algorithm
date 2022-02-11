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
