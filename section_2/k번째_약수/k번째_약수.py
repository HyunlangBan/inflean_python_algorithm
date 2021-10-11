def run(n, k):
  result = []
  for i in range(1, n+1):
    if not (n%i):
      result.append(i)
  
  if len(result) < k:
    return -1
  return(result[k-1])

n, k = map(int, input().split())
result = run(n,k)
print(result)

########### SOLUTION #############
## list를 사용하지 않고 cnt 사용
## 나도 for문을 끝까지 도는 것 보다 이 방법이 더 나은 것 같다.

n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
  if n%i==0:
    cnt += 1
  if cnt==k:
    print(i)
    break
else:       ####### for문에도 else가 있다! for문에서 break로 끝나지 않은 경우 수행
  print(-1)
           
