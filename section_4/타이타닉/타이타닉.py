n, m = map(int, input().split())
array = list(map(int, input().split()))

# 모든 구명보트에 최대인원이 탈 수 있을때 => 최소
array.sort(reverse=True)
cnt = 0
while array:
  if len(array)==1:
    array.pop()  # 굳이 pop할 필요는 없다.
    break

  max = array[0]
  min = array[-1]
  
  if max+min <= m:
    array.pop(0)
    array.pop(-1)
    cnt += 1
  else:
    # 최소와 더했을때도 m을 넘으므로 더이상 짝지을 수있는 경우가 없다.
    array.pop(0) 
    cnt +=1

print(cnt)
    
## 1씩 차이나게 틀리는 답들은 뭐지.... => len(array)==1인 경우 cnt 증가시키는걸 빼먹음

################## SOLUTION ####################
## 논리는 내가 푼 방식과 동일

from collections import deque ## 

# p.sort()
p=deque(p) ##

cnt = 0
while p:
  if len(p)==1:
    cnt += 1
    break
  if p[0]+p[-1] > limit:
    p.pop()
    cnt+=1
  else:
#     p.pop(0)
    p.popleft() ##
    p.pop()
    cnt += 1

print(cnt)

### list -> pop(0)일때 뒤의 index가 하나씩 이동해야 하므로 비효울적 -> deque를 이용하자(deque는 가르키는 idx 위치만 변경하는 방식)
