# Try - 🔺

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

## tmp는 닫히지 않은 막대기를 세는 stack으로 사용되어야 한다.
## tmp도 보고 for문을 돌면서 바로 이전 괄호도 확인하려면 index로 돌아야한다.
