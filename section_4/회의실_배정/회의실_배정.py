n = int(input())
meetings = []

for _ in range(n):
  s, e = map(int, input().split())
  meetings.append((s, e))

max_cnt = -1

for i in range(n):
  s, e = meetings[i]
  cnt = 1
  for j in range(i+1, n):
    n_s, n_e = meetings[j]
    if e <= n_s:
      cnt += 1
      e = n_e
  if cnt > max_cnt:
    max_cnt = cnt

print(max_cnt)
