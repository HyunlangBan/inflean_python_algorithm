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
