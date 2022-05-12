# Try 1 - ❌
## 어떻게 풀어야할지 감도 안잡힘
## stack 문제 !!!!! (큐, 스택 언제 써야할지 기억하자....)
## i번째 수보다 작은수가 없을때까지(+다른 조건) pop을 하는 것에 주의 -> if가 아니라 while!!!!!

# Try 2 - ❌
# 자릿수들 중 m개의 숫자를 제거 -> 가장 큰 수를 만들라

m, n = input().split()
n = int(n)

# 어차피 제거하는 갯수는 n개로 정해져있으므로 앞에 오는 수가 가장 크게 되어야함

# 가장 큰 수가 최대한 앞으로 와야함
# 가장 큰 수 앞에 있는 숫자들 중에 작은것부터 n개를 제거한다.

x = list(map(int, m))
max_idx = x.index(max(x))
idx = [0]*len(x)
# 빼면 idx를 1로 바꿔준다고 하자
behind = n - len(x[:max_idx])
cnt = 0
while cnt < n:
  min_idx = x.index(min(x))
  if min_idx < max_idx:
    if idx[min_idx]!= 1:
      idx[min_idx] = 1
      cnt += 1
      x[min_idx] = 9
  else:
    # max_idx 앞이 모두 제거되었거나 n이 max_cnt 앞에 있는 문자들보다 많을때
    if behind > 0:
      idx[min_idx]=1
      cnt += 1
      behind -= 1
    x[min_idx] = 9 # 값은 유지하되 min에서 빠져나가야함


for i in range(len(x)):
  if idx[i]==0:
    print(m[i], end='')
print()
    
## 가장 큰 수가 여러개 중복해서 나올떄(ex. 98999)는 생각을 안했네;
## 이 문제의 포인트는 stack을 사용해서 내림차순으로 정렬하는 것!
