n, k = map(int, input().split())

queue = [i for i in range(1, n+1)]

while len(queue) > 1:
  for _ in range(k-1):
    queue.append(queue.pop(0))

  queue.pop(0)

print(queue[0])
