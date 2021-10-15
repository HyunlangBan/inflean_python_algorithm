n = int(input())
matrix = []
max_sum = -1

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    if max_sum < sum(row):
        max_sum = sum(row)

for i in range(n):
    col_sum = 0
    for j in range(n):
        col_sum += matrix[j][i]
    if max_sum < col_sum:
        max_sum = col_sum

di_sum = 0
for i in range(n):
    di_sum += matrix[i][i]

if max_sum < di_sum:
    max_sum = di_sum

print(max_sum)
