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
    lt += 1  # xxxxx
    res = mid
  else:
    rt -= 1  # xxxxx

############ SOLUTION #############

def count(len):
  cnt=1
  ep=line[0]
  for i in range(1,n):
    if line[i]-ep>=len:
      cnt+=1
      cp=line[i]
  return cnt

n, c = map(int, input().split())
line = []
for _ in range(n):
  tmp=int(input())
  line.append(tmp)
line.sort()
lt=1
rt=line[n-1]

while lt<=rt:
  mid=(lt+rt)//2
  if count(mid)>=c:
    res=mid
    lt=mid+1
  else:
    rt=mid-1
    
print(res)
    
