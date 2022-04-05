# Try 1 - ✅
## 풀었지만 BFS로 풀지 않았음!

n = int(input())
farm = []
for _ in range(n):
  farm.append(list(map(int, input().split())))

res = 0
for i in range(n//2):
  s = n//2 - i
  e = n//2 + i + 1
  res += sum(farm[i][s:e])
  res += sum(farm[n-1-i][s:e])

res += sum(farm[n//2])
print(res)
  
