def run(n, k):
  result = []
  for i in range(1, n+1):
    if not (n%i):
      result.append(i)
  
  if len(result) < k:
    return -1
  return(result[k-1])

n, k = map(int, input().split())
result = run(n,k)
print(result)
