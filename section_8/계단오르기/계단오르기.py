def DFS(N):
  print(N, res)
  if res[N]:
    return res[N]
  res[N-2] = DFS(N-2)
  res[N-1] = DFS(N-1)
  res[N]=res[N-1]+res[N-2]
  ####### 보다는 res[N] = DFS[N-2] + DFS[N-1]가 낫다.
  return res[N] ######## 중요!!!!! 여기서도 return 해줘야함

n = int(input())
res = [0]*(n+1)
res[1] = 1
res[2] = 2
DFS(n)
print(res[n])



########## SOLUTION ############

def DFS(len):
  if dy[len]>0:
    return dy[len]
  if len==1 or len==2:
    return len
  else:
    dy[len]=DFS(len-1)+DFS(len-2)
    return dy[len]

n = int(input())
dy = [0] * (n+1)
print(DFS(n))
