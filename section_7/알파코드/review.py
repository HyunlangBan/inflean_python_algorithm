# Try 1 - ❌
## 예제만 끼워맞춘정도..? ㅠㅠ

a = list(map(int, input().split()))
result = []
cnt = 0

def DFS(L):
  global result
  global cnt
  if L==len(a):
    print(''.join(result))
    cnt += 1
    return

  res = chr(a[L]+64)
  result.append(res)
  DFS(L+1)
  result.pop()
  if L < len(a)-1:
    if a[L]<=2 and a[L+1]<=6:
      res = chr(a[L]*10+a[L+1]+64)
      result.append(res)
      DFS(L+2)
      result.pop()

DFS(0)
print(cnt)
