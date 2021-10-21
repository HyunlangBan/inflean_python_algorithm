n = int(input())
array = list(map(int, input().split()))

def find(prev):
  if len(array) == 1:
    last = array[0]
    if last-prev==prev_gap:
      print("L", end = '')
      return None

  l = array[0]
  r = array[-1]

  if r > prev and r-prev == prev_gap:
    prev = array.pop(-1)
    print("R", end = '')
    return prev

  elif l > prev and l-prev == prev_gap:
    prev = array.pop(0)
    print("L", end = '')
    return prev


if array[0] > array[-1]:
  prev_gap = array[0] - array[-1]
  prev = array.pop(-1)
  print("R", end = '')

else:
  prev_gap = array[-1] - array[0]
  prev = array.pop(0)
  print("L", end = '')

result = True

while prev:
  prev = find(prev)

print()
