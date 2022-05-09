# Try 1 - ✅
n = int(input())
a = []

for _ in range(n):
  h, w = map(int, input().split())
  a.append((w, h))

a.sort()
print(a)

# 본인보다 무거운 애들보다 키는 커야함
cnt = 1 # 가장 무거운 선수는 무조건 
for i in range(n-1):
  xh = a[i][1]
  for j in range(i+1, n):
    yh = a[j][1]
    if yh > xh:
      break
  else:
    print(a[i][0], a[i][1])
    cnt += 1

print(cnt)

# Try 2 - ✅
# 무게가 가벼운 기준으로 정렬하고
# 무게가 가벼운 선수들은 무게가 무거운 다른 선수들보다 키가 가장 커야한다.
# 가장 무거운 선수는 무조건 선발되므로 cnt는 1부터 시작한다.
n = int(input())
players = []
for _ in range(n):
  h, w = map(int, input().split())
  players.append((w, h))

players.sort()
# print(players)

cnt = 1
for i in range(n-1):
  w, h = players[i][0], players[i][1]
  max_h = h
  for j in range(i+1, n):
    y_w, y_h = players[j][0], players[j][1]
    # print(h, y_h)
    max_h = max(max_h, y_h)
    # print(max_h)
  if max_h ==h:
    cnt += 1

print(cnt)
