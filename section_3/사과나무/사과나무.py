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
