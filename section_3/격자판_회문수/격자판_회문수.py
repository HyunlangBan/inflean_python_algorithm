m = [list(map(int, input().split())) for _ in range(7)]
size = 7
start = 0
cnt = 0
word = 5

for i in range(3):
    x_res = 1
    y_res = 1
    for j in range(size//2-1):
        if m[i][j] != m[i][word-j]:
            x_res = 0
            break

        if m[j][i] != m[word-j][i]:
            y_res = 0
            break
    cnt = cnt+x_res+y_res

print(cnt)


############# SOLUTION #############

board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+5]
        if tmp==tmp[::-1]:
            cnt+=1
            
        ## 세로로는 리스트가 아니므로 슬라이스 불가
        for k in range(2):
            if board[i+k][j]!=board[i+5-k-1][j]:
                break
        else:
            cnt+=1
print(cnt)
