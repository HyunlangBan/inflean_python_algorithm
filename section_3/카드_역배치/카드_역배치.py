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
    print(a, end=' '
