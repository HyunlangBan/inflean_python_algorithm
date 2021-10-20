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
