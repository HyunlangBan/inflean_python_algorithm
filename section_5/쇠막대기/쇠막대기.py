# 현재 괄호의 다음 값을 따진다.
# ( 의 다음이 ( 이면 막대기의 시작 지점이다. ) 이면 레이저이다.
# ) 의 앞이 ) 이면 쇠막대기의 끝 지저밍다.

## stack 사용!
## ( 는 무조건 stack에 append!
## ) 일때 앞이 ( 이면 레이저이므로 ( 를 pop한다. -> stack에 남아있는 것의 갯수를 결과 값에 더한다.
## ) 의 앞이 ) 이면 막대기의 끝 지점이므로 가장 윗 막대기 ) 를 지우고 결과 값에 1을 더한다.

s = input()
stack = []
cnt = 0
for i in range(len(s)):
  if s[i] == '(':
    stack.append(s[i])
  else:
    stack.pop()
    # 레이저인 경우
    if s[i-1] == '(':
      cnt += len(stack)
    # 쇠막대의 끝인 경우
    else:
      cnt += 1
