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
