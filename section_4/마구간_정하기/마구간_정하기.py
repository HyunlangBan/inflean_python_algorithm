n, c = map(int, input().split())
houses = []

for _ in range(n):
  houses.append(int(input()))

houses.sort()

lt = houses[1]-houses[0]
rt = houses[-1]-houses[0]

def count(distance):
# 어떻게 세야할지 모르겠다.
  pass
    

res = 0

while lt<=rt:
  mid = (lt+rt)//2
  if count(mid) >= c:
    lt += 1
    res = mid
  else:
    rt -= 1
