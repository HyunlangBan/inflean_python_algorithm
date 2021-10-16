n = int(input())
size = n+2
matrix = []

for i in range(size):
    if i == 0 or i == size-1:
        array = [0]*(size)
    else:
        array = [0] + list(map(int, input().split())) + [0]
    matrix.append(array)


visited = [[False]*size for _ in range(size)]
cnt = 0

for i in range(1, size-1):
    for j in range(1, size-1):

        if visited[i][j]:
            continue

        p = matrix[i][j]
        left = matrix[i-1][j]
        right = matrix[i+1][j]
        up = matrix[i][j-1]
        down = matrix[i][j+1]

        if p > up and p > down and p > left and p > right:
            cnt += 1
            visited[i-1][j] = True
            visited[i+1][j] = True
            visited[i][j-1] = True
            visited[i][j+1] = True

print(cnt)
