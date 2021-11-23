############# SOLUTION ##############
def DFS(L, sum):
  global res
  if L==n:
    if 0<sum<=s:      ## 양수만 보는 이유: 어차피 음수일때와 대칭이므로
      res.add(sum)
  else:
    DFS(L+1, sum+G[L]) ## 추를 왼쪽에 놓는 경우
    DFS(L+1, sum-G[L]) ## 추를 오른쪽에 놓는 경우
    DFS(L+1, sum)      ## 추를 안놓는 경우
    
n = int(input())
G = list(map(int, input().split()))
s = sum(G)
res = set()
DFS(0, 0)
print(s-len(res))
