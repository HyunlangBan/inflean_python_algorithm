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

  
############# SOLUTION ###############
## dict에서 get함수를 써보자

a = input()
b = input()
str1 = dict()
str2 = dict()

for x in a:
  str[x] = str1.get(x, 0) + 1
for x in b:
  str2[x] = str2.get(x, 0) + 1

for i in str1.keys():
  if i in str2.keys():
    if str1[i] != str2[i]:
      print("N0")
      break
  else:
    print("NO")
    break
else:
  print("YES")

## 개선 코드
sH = dict()
for x in a:
  sH[x] = sH.get(x, 0) + 1
  
for x in b:
  sH[x] = sH.get(x, 0) - 1

for x in a:
  if sH.get(x) > 0:
    print("NO")
    break
else:
  print("YES")
