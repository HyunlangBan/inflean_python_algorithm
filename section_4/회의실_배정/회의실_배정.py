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

######### SOLUTION ###########
## 회의가 끝나는 시간을 기준으로 정렬해야함
## 회의가 빨리 시작되는 것이 중요한게 아니라 회의가 빨리 끝나서 최대한 많은 회의를 할 수 있는 것이 중요함

n = int(input())
meeting = []

for i in range(n):
  s, e = map(int, input().split())
  meeting.append((s,e))

meeting.sort(key=lambda x:(x[1], x[0]))  # 끝나는 시간을 기준으로 하여 정렬
et = 0
cnt = 0
for s, e in meeting:
  if s >= et:
    et = e
    cnt += 1

print(cnt)
