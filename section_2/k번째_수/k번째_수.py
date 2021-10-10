test_cases = int(input())

for _ in range(test_cases):
    N, s, e, k = map(int, input().split())
    array = list(map(int, input().split()))

    split = sorted(array[s - 1:e])
    print(split[k - 1])
