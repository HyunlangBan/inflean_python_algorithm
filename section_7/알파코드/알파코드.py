############# SOLUTION ###############
def DFS(L, P):
  global cnt
  if L==n:
    cnt += 1
    for j in range(P):
      print(chr(res[j]+64), end=''). # 65 = A
    print()
  else:
    for i in range(1, 27):
      if code[L] == i:      ## 한자리숫자
        res[P] = i
        DFS(L+1, P+1)
      else i>=10 and code[L]==i//10 and code[L+1]==i%10:
        res[P]=i
        DFS(L+2, P+1)

code = list(map(int, input()))
n = len(code)
code.insert(n, -1)        ## code의 마지막 idx에서 두자리수를 확인할때 out of index 에러가 나기 때문에
res = [0] * n
cnt = 0
DFS(0, 0)
print(cnt)
