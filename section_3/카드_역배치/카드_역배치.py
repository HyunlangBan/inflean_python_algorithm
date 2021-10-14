array = [i for i in range(21)]

for _ in range(10):
    a, b = map(int, input().split())
    front = array[:a]
    mid = array[a:b+1]
    new_mid = []
    for i in range(len(mid)-1, -1, -1):
        new_mid.append(mid[i])
    end = array[b+1:]
    array = front+new_mid+end
    
for a in array[1:]:
    print(a, end=' ')
          
########## SOLUTION ###########

a = list(range(21) ## 간단하다
for _ in range(10):
     s, e = map(int, input().split())
     for i in range((e-s+1)//2):
         a[s+i], a[e-i] = a[e-i], a[s+i]  # 이렇게 swap하는걸 시도했었는데 안됐던 이유는 범위를 반으로 안나눠서이다.
     a.pop(0)
     for x in a:
         print(x, end=' ')
