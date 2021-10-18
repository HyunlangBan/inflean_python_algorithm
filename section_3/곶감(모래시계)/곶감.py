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
### 테스트 5개중 3개 정답


########### SOLUTION ############
## 배열을 어떻게 회전할지 궁금했는데 생각하지 못했던 pop, insert를 활용했다.

for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())
                
res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)
