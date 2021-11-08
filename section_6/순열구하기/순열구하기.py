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
