n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# new_list = a+b
# new_list.sort()
#
# print(new_list)
# 이렇게 풀었다가 대충 푼 것 같아서 다른 방법을 생각해봄

new_list = []
while True:
    if len(a) == 0 and len(b) == 0:
        break
    elif len(a) == 0:
        new_list.extend(b)
        break
    elif len(b) == 0:
        new_list.extend(a)
        break

    if a[0] <= b[0]:
        small = a.pop(0)
    else:
        small = b.pop(0)
    new_list.append(small)
print(new_list)

########## SOLUTION ###########
## sort()는 NlogN의 시간 복잡도를 가짐
## 이미 오름차순으로 정렬된 것을 정렬하는 것은 N번만에 가능
## 난 요소를 제거해가면서 했고 답안은 인덱스를 더해나가면서 풀었다. 

p1=p2=0
c=[]
while p1<n and p2<m:
    if a[p1]<=b[p2]:
        c.append(append[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]

print(c)
