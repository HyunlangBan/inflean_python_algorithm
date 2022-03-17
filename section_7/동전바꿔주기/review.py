# Try 1 - ❌
## 같은 동전이 여러개이니 조합으로 접근하면 안되는 문제였다. 
t = int(input())
k = int(input())
a = []
for _ in range(k):
  x, y = map(int, input().split())
  a.extend([x]*y)

a.sort(reverse=True)
ch = [0]*len(a)
cnt = 0
print(a)

def DFS(L, total):
  global cnt
  if total == t:
    cnt += 1
    return

  for i in range(L, len(a)):
    if not ch[i]:
      ch[i]=1
      DFS(L+1, total+a[i])

DFS(0, 0)
print(cnt)

# Try 2 - ❌
## 답을 확인하고 기억을 더듬어가면서 작성했는데 정답이 안나와서 계속 고민했다.....
## 문제는! for문에서 동전을 고를때 고르지 않는 경우도 따져야 했음!
t = int(input())
k = int(input())
a = []
for _ in range(k):
  x, y = map(int, input().split())
  a.append((x, y))

cnt = 0
def DFS(L, total):
  global cnt
  if L==k:
    if total == t:
      cnt += 1
    return

  for i in range(1, a[L][1]+1):   ### range에서 1부터 시작하면 안된다! 0도 되어야 함!!
    DFS(L+1, total+(a[L][0]*i))
    
DFS(0, 0)
print(cnt)
## 추가적으로 total > t인 경우는 리턴하여 cut-edge 해주어야함!
