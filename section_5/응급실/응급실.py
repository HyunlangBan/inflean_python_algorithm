# 순서가 밀린다고 해서 진료 순서가 바뀌는것이 아니라 실제로 우선순위가 높은 환자가 진료를 받아야 진료순서 +1이 되는것이었다.

n, m = map(int, input().split())
a = list(map(int, input().split()))
line = [i for i in range(n)]
wait = 0

while len(line)>1:
  patient_n = line.pop(0)
  severity = a.pop(0)
  if severity < max(a):
    line.append(patient_n)
    a.append(severity)
  else:
    wait += 1
    if patient_n == m:
      break
    
print(wait)
