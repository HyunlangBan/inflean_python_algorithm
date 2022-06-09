# Try 1 - ❌ TimeOut
## 파스칼 수식으로 만들어내는거 생각하기가 어렵다....

# 위의 두개를 더한 값이 위에 저장

n, f = map(int, input().split())
# n개의 순열을 만든다.
res = [0]*n
ch = [0]*n

def check_sum(a):
  result = []
  for i in range(len(a)-1):
    result.append(a[i]+a[i+1])
  return result
  
def DFS(L):
  if L==n:
    ret = check_sum(res)
    while len(ret)>1:
      ret = check_sum(ret)
    if ret[0]==f:
      print(res)
      exit(0)
    return

  for i in range(n):
    if ch[i]==0:
      ch[i]=1
      res[L]=i+1
      DFS(L+1)
      ch[i]=0

DFS(0)

# Try 2 - ❌
## 풀이 방법이 또 생각이 안나서 풀이 참고 보고 풀었다.
## 근데 문제를 잘못 이해했다;; 1~10까지 중복으로 가능한 줄 알았는데 1~N까지고 중복 포함 안됐음
## 다음엔 itertools 활용한 풀이로 풀어야지

n, f = map(int, input().split())
a = [0]*n
mul = [0]*n
mul[0] = 1
res = []
for i in range(1, n):
  mul[i] = mul[i-1]*(n-i)/i

def check(a):
  sum = 0
  for i in range(n):
    sum += a[i]*mul[i]
  return sum

def DFS(L):
  global res
  if L==n:
    if check(a) == f:
      print(a, check(a))
      res.append(a)
    return

  for i in range(1, 11):
    a[L] = i
    DFS(L+1)

DFS(0)
print(res)
