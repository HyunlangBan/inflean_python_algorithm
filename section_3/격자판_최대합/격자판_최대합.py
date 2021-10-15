n = int(input())
matrix = []
max_sum = -1

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    if max_sum < sum(row):
        max_sum = sum(row)

for i in range(n):
    col_sum = 0
    for j in range(n):
        col_sum += matrix[j][i]
    if max_sum < col_sum:
        max_sum = col_sum

di_sum = 0
for i in range(n):
    di_sum += matrix[i][i]

if max_sum < di_sum:
    max_sum = di_sum

print(max_sum)

############# SOLUTION ##############
## 훨씬 답이 간결
## 난 대각선 반대편 계산을 빼먹었다;;

a = [list(map(int, input().split())) for _ in range(n)] ## 간단하다!
largest=-2147000000
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2
        
sum1=sum2=0
for i in range(n):
    sum1+=a[i][j]
    sum2+=a[i][n-i-1]
if sum1>largest:
    largest=sum1
if sum2>largest:
    largest=sum2
    
print(largest)
    
       
