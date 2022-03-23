# Try 1 - ❌

k = int(input())
a = list(map(int, input().split()))
ch = [0]*k

# 왼쪽, 오른쪽 부분집합 찾기
res = set()
def DFS(L, sum):
  global res
  if L==k:
    res.add(sum)
    for i in range(k):
      if ch[i]==0:
        res.add(abs(sum - a[i]))
    return

  ch[L] = 1
  DFS(L+1, sum+a[L])
  ch[L]=0
  DFS(L+1, sum)

DFS(0, 0)
res = list(res)
res.pop(0)
result = sum(a)-len(res)
print(result)

# 어떻게 푸는지 대충 느낌은 왔는데 ......... 해답을 못찾음 ㅜ
# sum에서 오른쪽 부분집합은 +로, 왼쪽 부분집합은 -로 합산해주면 되는 문제였다!
