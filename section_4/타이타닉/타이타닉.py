n, m = map(int, input().split())
array = list(map(int, input().split()))

# 모든 구명보트에 최대인원이 탈 수 있을때 => 최소
array.sort(reverse=True)
cnt = 0
while array:
  if len(array)==1:
    array.pop()
    break

  max = array[0]
  min = array[-1]
  
  if max+min <= m:
    array.pop(0)
    array.pop(-1)
    cnt += 1
  else:
    # 최소와 더했을때도 m을 넘으므로 더이상 짝지을 수있는 경우가 없다.
    array.pop(0) 
    cnt +=1

print(cnt)
    
