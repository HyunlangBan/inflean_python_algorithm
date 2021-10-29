def create_dict(word):
  d = {}
  for w in word:
    try:
      if d[w]:
        d[w] += 1
    except KeyError:
      d[w] = 1
  return d

w1 = create_dict(input())
w2 = create_dict(input())

print(w1)
print(w2)

if w1 == w2:
  print("YES")
else:
  print("NO")
