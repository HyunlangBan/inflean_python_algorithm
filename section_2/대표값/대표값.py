n = int(input())
array = list(map(int, input().split()))
mean = round(sum(array)/n)
result = [score-mean for score in array]

min = min(map(abs, result))

if min in result:
    idx = result.index(min)
else:
    idx = result.index(-min)
print(mean, idx+1)

######### SOLUTION ##########
# 최소값을 직접 구하는 방식을 선택

n = int(input())
a = list(map(int, input().split()))
# ave = round(sum(a)/n)   ###### 문제 오류 -> round half up 방식이 아니라 round_half_even(.5일때 짝수쪽으로 근사) 방식임 
ave = int((sum(a)/n) + 0.5)
min=2147000000

for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
     elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)
