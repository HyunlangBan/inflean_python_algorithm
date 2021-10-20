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
