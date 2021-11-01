n = int(input())
res = []

def d(number):
  if number == 0:
    return number
  
  x = number//2 #몫
  y = number%2 #나머지
  d(x)
  res.append(y)

d(n)
res = ''.join(map(str, res))
print(res)
