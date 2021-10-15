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
