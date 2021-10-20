n = int(input())
info = []

for i in range(n):
  h, w = map(int, input().split())
  info.append((h, w))

cnt = n
for h, w in info:
  for h2, w2 in info:
    if h<h2 and w<w2:
      cnt -= 1

print(cnt)


############### SOLUTION ################
## 키순으로 정렬
## 맨 위를 제외하고 자신보다 키가 큰 사람들보다 몸무게가 높아야한다.
## 이중포문을 피하기 위해서 최대값을 구하는 방식을 선택한다. (지금까지의 범위에서 최대값이 되는지)

n = int(input())
body = []

for i in range(n):
  a, b = map(int, input().split())
  body.append((a,b))
  
body.sort(revers=True)
largest = 0
cnt = 0
for x, y in body:
  if y > largest:
    largest = y
    cnt += 1
  
print(cnt)
