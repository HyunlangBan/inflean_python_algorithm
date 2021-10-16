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


############ SOLUTION ################
## 가장자리 0으로 초기화 하는 법을 알아두자

n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]

# 가장자리 초기화
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0,0)
    x.append(0)

cnt=0

# 4방향 탐색을 할 때 유용한 방법
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):   ## all: 모든 조건이 참일때
            cnt+=1
print(cnt)
