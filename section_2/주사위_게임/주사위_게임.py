n = int(input())

def calculate(array):
    max_point = -1
    for i in range(7):
        if array[i] == 3:
            return 10000+(i*1000)
        elif array[i] == 2:
            return 1000+(i*100)
        elif array[i] == 1:
            max_point = i
    return max_point * 100


prize = []
for _ in range(n):
    array = [0]*7
    points = list(map(int, input().split()))
    for point in points:
        array[point] += 1
    prize.append(calculate(array))

print(max(prize))
