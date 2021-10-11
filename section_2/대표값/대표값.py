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
n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n)
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
