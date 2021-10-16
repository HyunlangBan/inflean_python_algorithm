n = int(input())
trees = [list(map(int, input().split())) for _ in range(n)]
mid = n//2
apples = 0

for row in range(mid+1):
    left_col = mid - row
    right_col = mid + row
    for col in range(left_col, right_col+1):
        apples += trees[col][row]
        if row != mid:
            apples += trees[col][n-row-1]

print(apples)

########## SOLUTION ###########
## 범위를 1씩 +,-함

res = 0
s=e=n//2
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)
