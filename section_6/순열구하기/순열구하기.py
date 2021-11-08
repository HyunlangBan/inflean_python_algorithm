## 중복 순열밖에 모르겠음
## 왜 같은 수가 반복되는 결과가 나올까((1,1),(1,1)(1,1),(1,2)...)

n, m = map(int, input().split())
a = [0]*(m+1)

def DFS(L, num):
  if L > m:
    for i in range(1, m+1):
      print(a[i], end = ' ')
    print()
    return

  a[L] = num
  for i in range(1, n+1):
    DFS(L+1, i)

DFS(0, 0)


########### SOLUTION ############
## 중복을 확인하는 checklist를 만들어야함

def DFS(L):
  global cnt
  if L==m:
    for j in range(L):
      print(res[j], end=' ')
    print()
    cnt += 1
  
  else:
    for i in range(1, n+1):
      if ch[i] == 0:
        cn[i] = 1
        res[L] = i
        DFS(L+1)
        ch[i] = 0

res = [0] * n
ch = [0] * (n+1)
cnt = 0
DFS(0)
print(cnt)
