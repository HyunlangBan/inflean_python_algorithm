n = int(input())
words = [input() for _ in range(n)]
written = [input() for _ in range(n-1)]

for w in words:
  if w not in written:
    print(w)
