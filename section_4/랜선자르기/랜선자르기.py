############ SOLUTION ##############

## 결정 알고리즘
# 답이 특정 범위안에 있다는 것을 알 수 있고 그 범위 내에서 이분 검색을 하면서 답을 확인하는 작업

## 랜선의 길이는 1 ~ 주어진 랜선의 최대길이 범위까지 가능하다.
## 랜선의 최대 길이를 찾을때까지 가능한 랜선의 길이를 계속 늘려나간다.

def count(len):
  cnt = 0
  for x in line:
    cnt += (x//len)
  return cnt

k, n = map(int, input().split())
lines = []
res = 0
largest = 0

for i in range(k):
  tmp = int(input())
  lines.append(tmp)
  largest = max(largest, tmp)  # largest와 tmp를 비교하여 큰 수를 largest에 넣는다.
  
lt = 1
rt = largest
while lt <= rt:
  mid = (lt+rt)//2
  if count(mid) >= n:
    res = mid
    lt = mid+1
  else:
    rt = mid-1
print(res)
