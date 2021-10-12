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

## FAIL -> TIMEOVER (제한시간 1초)

########## SOLUTION ###########
# 에라토스테네스 체
n = int(input())
ch = [0] * (n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i] == 0:   # value가 0이면 소수
        cnt += 1
        for j in range(i, n+1, i):   ### Step (소수의 배수들 check)
            ch[j] = 1
