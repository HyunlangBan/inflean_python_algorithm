########## SOLUTION #############
## Cut Edge Tech
## 부분집합 사용 문제
## 모든 부분 집합을 만들고, 부분집합의 합이 한도에 적합한지 확인

def DFS(L, sum, tsum):
  global result
  
  if sum + (total - tsum) < result:  # 부분집합의 합 + (선택이 남은 바둑이들의 무게 합)
    return  # 끝까지 돌아봤자 지금까지 구한 최대 값에 못미치므로 소용이 없음
  
  if sum > c:
    return
  
  if L == n:
    if sum > result:
      result = sum
  else:
    DFS(L+1, sum+a[L], tsum+a[L])  ## 부분집합에 포함
    DFS(L+1, sum, tsum+a[L])       ## 부분집합에 미포함

c, n = map(int, input().split())
a = [0] * n
result = -2147000000 # 가장 큰 값을 찾아야 하므로
                              
for i in range(n):
  a[i] = int(input())
                              
total = sum(a)
DFS(0, 0, 0)
print(result)
