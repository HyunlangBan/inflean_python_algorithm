# Try - ๐บ

s = list(input())
tmp = []
cnt = 0
for i in s:
  print(tmp)

  if i == '(':
    tmp.append(i)
  else:
    if tmp and tmp[-1]=='(':
      tmp.pop()
      cnt += len(tmp)
      
print(cnt)

## tmp๋ ๋ซํ์ง ์์ ๋ง๋๊ธฐ๋ฅผ ์ธ๋ stack์ผ๋ก ์ฌ์ฉ๋์ด์ผ ํ๋ค.
## tmp๋ ๋ณด๊ณ  for๋ฌธ์ ๋๋ฉด์ ๋ฐ๋ก ์ด์  ๊ดํธ๋ ํ์ธํ๋ ค๋ฉด index๋ก ๋์์ผํ๋ค.
