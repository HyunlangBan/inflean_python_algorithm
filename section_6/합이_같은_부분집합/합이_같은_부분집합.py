######### SOLUTION ###########
## 전체 sum - 한 부분집합의 sum = 나머지의 부분집합의 sum

def DFS(L, sum): # L: 인덱스 번호(Level)
  if sum > total//2:   ## sum을 누적하다가 절반보다 커져 버림
                       ## sum == total//2는 n이 홀수일때는 성립되지 않음 
    return
  
  if L==n:
    if sum == (total-sum):
      print("YES")
      sys.exit(0)
      
  else:
    DFS(L+1, sum+a[L]) # a[L] 사용
    DFS(L+1, sum)      # a[L] 미사용
  
n = int(input())
a = list(map(int, input().split()))
total = sum(a)
DFS(0, 0)
print("NO")
