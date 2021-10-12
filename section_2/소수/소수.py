n = int(input())
# 소수: 1과 자기 자신만으로 나누어지는 수
# 2나 3으로 나눠진다면 소수가 아니다? XXXX 반례) 5*5

count = 1  # 1포함
result = True
for i in range(2, n+1):
    for j in range(1, i):
        if not i%j:
            result = False
    if result:
        count += 1

print(count)

## TIMEOVER (제한시간 1초)
