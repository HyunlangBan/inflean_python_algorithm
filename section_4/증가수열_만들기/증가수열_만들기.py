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

############### SOLUTION ##################
## pop을 쓰지 않고 idx를 변화시키는 방식을 선택

lt = 0
rt = n-1
last = 0

res = ""
tmp = []

while lt <= rt: ###
  if a[lt] > last:
    tmp.append((a[lt], 'L'))
  if a[rt] > last:
    tmp.append((a[rt], 'R'))
  tmp.sort() # 증가수열의 다음항을 선택하기 위해 정렬
  
  if len(tmp) == 0:
    break
  else:
    res = res + tmp[0][1]
    last = tmp[0][0]
    if tmp[0][1] == 'L':
      lt += 1
    else:
      rt -= 1
      
  tmp.clear()
 
print(len(res))
print(res)
