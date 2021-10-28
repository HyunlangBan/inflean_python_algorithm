n = int(input())
words = [input() for _ in range(n)]
written = [input() for _ in range(n-1)]

for w in words:
  if w not in written:
    print(w)

################ SOLUTION #################
## 해쉬를 사용하지 않고 풀어서 해쉬 풀이방법을 참고하자

p = dict()
for i in range(n):
  word = input()
  p[word] = 1

for i in range(n-1):
  word = input()
  p[word] = 0
  
for key, value in p.items():
  if value == 1:
    print(key)
    break
