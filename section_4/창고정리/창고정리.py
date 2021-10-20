l = int(input())
array = list(map(int, input().split()))
m = int(input())

def move(max_h, min_h):
  max_idx = array.index(max_h)
  min_idx = array.index(min_h)

  array[max_idx] -= 1
  array[min_idx] += 1

for _ in range(m):
  min_h = min(array)
  max_h = max(array)

  move(max_h, min_h)

print(max(array) - min(array))

############# SOLUTION ###############
## 최대, 최소를 찾기 위해 매번 sorting을 하라.
L = int(input())
a = list(map(int, input().split()))
m = int(input())
a.sort()
for _ in range(m):
  a[0] += 1
  a[L-1] -= 1
  a.sort()
  
print(a[L-1] - a[0])
