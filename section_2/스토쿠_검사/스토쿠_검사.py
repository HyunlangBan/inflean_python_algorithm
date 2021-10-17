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


############## SOLUTION ################

def check(a):
    for i in range(9):
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    for i in range(3):         ## 와우 사중for문..
        for j in range(3):
            ch3=[0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]=1
            if sum(ch3)!=9:
                return False
    return True


a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")



