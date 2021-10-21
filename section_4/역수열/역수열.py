n = int(input())
array = list(map(int, input().split()))

# 항상 가장 작은 수가 들어오기 때문에 앞에는 주어진 수만큼의 큰 수가 빈 자리에 들어가야함
result = [0] * n

for i in range(n):
  # i+1보다 큰수의 갯수는 array[i]
  cnt = 0
  for j in range(n):
    if cnt == array[i] and not result[j]:
      result[j] = i+1
      break
    if not result[j]:
      cnt += 1

for n in result:
  print(n, end=' ')
print()


############## SOLUTION ##############
## 빈자리 찾는 다른 방법도 참고하기

for i in range(n):
  for j in range(n):
    if a[i]==0 and seq[j]==0:
      seq[j]=i+1
      break
    elif seq[j]==0:   ### 빈자리를 찾으면 값을 뺀다.
      a[i]-=1
