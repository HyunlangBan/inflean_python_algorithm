n, m = input().split()
m = int(m)

from collections import deque
# 제일 큰 수가 앞에서 m개를 제거했을때 있다면 앞 수들을 모두 제거

# 제일 큰 수를 위해서 앞에서 m개 이상을 제거해야 한다면 그 다음 큰수를 확인
n = deque(n)
desc_sort = sorted(n)
largest = desc_sort[-1]

cnt = 0
while cnt <= m:
  max_idx = n.index(largest)
  if max_idx <= m:
    if n[0] == largest:
      # n.pop(n.index(min(n)))
      # 가장 앞에오는 큰수 다음에는 남은 것중 최대가 와야함
      for i in range(2, len(n)):
        if n[1] < n[i]:
          n.remove(n[1])
          cnt += 1
          break
        else:
          n.remove(min(n))
    else:
      n.popleft()
    cnt += 1 
  # find next_max
  else:
    desc_sort.pop()
    largest = desc_sort[-1]
    continue

for i in n:
  print(i, end='')
    
############## 포기

############## SOLUTION ################
