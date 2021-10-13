n = int(input())

def calculate(array):
    max_point = -1
    for i in range(7):
        if array[i] == 3:
            return 10000+(i*1000)
        elif array[i] == 2:
            return 1000+(i*100)
        elif array[i] == 1:
            max_point = i
    return max_point * 100


prize = []
for _ in range(n):
    array = [0]*7
    points = list(map(int, input().split()))
    for point in points:
        array[point] += 1
    prize.append(calculate(array))

print(max(prize))

########## SOLUTION ###########
## 더 간단

n = int(input())
res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a,b,c = map(int, tmp)
    if a==b and b==c: # 3개가 같음
        money=10000+a*1000
    elif a==b or a==c:
        money=1000+(a*100)
    elif b==c:
        money=1000+(b*100)
    else:
        money=c*100
    if money>res:
        res=money
        
print(res)
