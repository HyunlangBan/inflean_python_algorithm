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
    
############## 포기. 문제풀이 아이디어를 못찾음

############## SOLUTION ################
## 앞 숫자가 자기보다 작으면 제거하고 들어감 -> stack(LIFO)
## 내림차순으로 쌓이게됨

num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []

for x in num:
  # stack에 값이 있고, 삭제할 갯수가 남아있으며 마지막으로 들어간 숫자가 현재보다 작은 경우
  while stack and m > 0 and stack[-1] < x:
    stack.pop()
    m -= 1
  stack.append(x)
  
# m을 소진시키지 않고 다 돈경우 -> 뒤에 있는 숫자들을 지운다(내림차순이므로)
if m != 0:
  stack = stack[:-m]
  
res = ''.join(map(str, stack))
print(res)
