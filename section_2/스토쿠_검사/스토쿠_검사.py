m = [list(map(int, input().split()))]
# 각 행 확인
solved = True
for row in range(9):
    if len(set(row)) < 9:
        solved = False
        exit()

# 각 열 확인
for i in range(9):
    check = set()
    for j in range(9):
        check.add(m[j][i])
    if len(check) < 9:
        solved = False
        exit()

# 각 정사각형 확인
# 모르겠다...............
