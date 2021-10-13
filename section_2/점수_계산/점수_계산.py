n = int(input())
grades = list(map(int, input().split()))
array = [0] * n
point = 0
for i in range(n):
    if grades[i] == 0:
        point = 0
    elif grades[i] == 1:
        point += 1
        array[i] = point

print(sum(array))
