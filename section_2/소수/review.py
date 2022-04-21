## Try1 => ❌❌❌ TIMEOUT ❌❌❌

n = int(input())
cnt = 0
for i in range(2, n+1):
  for j in range(2, i):
    if i%j==0:
      # print(f"{i%j}")
      break
  else:
    cnt += 1
print(cnt)


## Try2 => ❌
# 첫번째 복병: 여전히 Timeout
# 두번째 복병: timeout은 어찌저찌 해결했는데 문제 예시만 풀리는 매직..

n = int(input())

# 1과 자기 자신으로만 나눠지는 수 -> 소수
# 소수의 배수는 소수가 아니다.
ch = [0]*(n+1)
for i in range(2, n+1):
  if ch[i]:
    break
  else:
    for j in range(2, i):
      if i%j==0:
        break
    else:
      # 소수 i
      cnt = n//i
      for x in range(2, cnt+1):
        ch[i*x] = 1

res = 0
for k in range(2, n):
  if ch[k]==0:
    res += 1
print(res)
