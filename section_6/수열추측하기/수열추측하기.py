############ SOLUTION ##############
## n이 4라면 4로 만들수 있는 순열을 다 해보는 방법 -> 너무 많은 가지수가 나옴, 공식을 찾아보자

def DFS(L, sum):
  if L==n and sum==f:
    for x in p:
      print(x, end=' ')
    print()
    sys.exit(0)
    
  else:
    for i in range(1, n+1):
      if ch[i] == 0:
        ch[i] = 1
        p[L] = i
        DFS(L+1, sum+(p[L]*b[L]))
        ch[i]=0

p = [0]*n  # 순열
b = [1]*n  # 맨 끝은 바꿀 필요가 없음
ch = [0]*(n+1)  # 중복 체크
for i in range(1, n):
    b[i] = b[i-1]*(n-i)//i
DFS(0,0)
