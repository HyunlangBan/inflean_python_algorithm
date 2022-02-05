## Try1 - ✅
cards = [i for i in range(21)]

for _ in range(10):
  a, b = map(int, input().split())
  x = cards[:a]
  y = cards[b:a-1:-1]
  z = cards[b+1:]
  
  cards = x+y+z

for c in cards[1:]:
  print(c, end=' ')
