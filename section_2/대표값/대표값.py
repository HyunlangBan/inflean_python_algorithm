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
