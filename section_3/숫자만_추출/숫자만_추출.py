string = input()
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
only_number = ''

for s in string:
    if s in number:
        only_number += s

only_number = int(only_number)

result = 0
for i in range(1, only_number+1):
    if only_number%i == 0:
        result += 1

print(only_number)
print(result)

########### SOLUTION ############
## .isdecimal
## 문자->숫자 변환 계산

s = input()
res = 0

for x in s:
    if x.isdecimal():   # 0~9까지의 숫자인지 확인한다.
        res = res*10 + int(x)
# 이하 방법 동일
