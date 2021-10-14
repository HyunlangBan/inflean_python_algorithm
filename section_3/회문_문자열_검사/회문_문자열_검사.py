n = int(input())

for _ in range(n):
    word = input()
    word = word.lower()
    if word == word[::-1]:
        print('YES')
    else:
        print('NO')
        
########### SOLUTION ############
## 절반만 돌아도 된다!!

for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2):    ## l, e, v, e, l -> 글자수 홀수일때 가운데는 혼자이므로 비교할 필요 없음
        if s[j] != s[-1-j]:
            print("NO")
            break         ## 아닌 경우 발생하면 바로 break 
        else:
            print("YES")
