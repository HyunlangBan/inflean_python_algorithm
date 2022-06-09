# Review - ✅
n, m = map(int, input().split())

# n번까지의 구술 중 중복을 허락하여 m번을 뽑아 일렬로 나열
res = [0]*m
cnt = 0

def DFS(L):
  global cnt
  if L==m:
    print(res[0], res[1])
    cnt += 1
    return

  for i in range(1, n+1):
    res[L] = i
    DFS(L+1)

DFS(0)
print(cnt)
