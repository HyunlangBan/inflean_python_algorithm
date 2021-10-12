def digit_sum(num):
    result = sum(map(int, num))
    return result

n = int(input())
array = list(input().split())
max_sum = -1
for i in range(n):
    result = digit_sum(array[i])
    if result > max_sum:
        max_sum = result
        number = array[i]
print(number)

########### SOLUTION ############

def digit_sum(x):
    sum = 0
    while x>0:
        sum += x%10
        x = x//10
    return sum

max = -2147000000
# 이하 동일
