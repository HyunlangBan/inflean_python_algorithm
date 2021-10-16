n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
for _ in range(m):
    col, direction, num = map(int, input().split())
    array = matrix[col-1]
    if direction == 0:
        # 왼쪽 num개가 넘어간다
        matrix[col-1] = array[num:]+array[:num]
    else:
        p = n-num
        matrix[col-1] = array[p:]+array[:p]

l_end, r_end = 0, n-1
result = 0
for col in range(n//2+1):
    lp = l_end + col
    rp = r_end - col
    for i in range(lp, rp+1):
        result += matrix[col][i]
        if col != n//2:
            result += matrix[n-1-col][i]
print(result)

### 하.. 행, 열이 너무 헷갈린다.
