def reverse(x):
    reversed = x[::-1]
    return int(reversed)

def isPrime(x):
    prime = True
    if x == 1:
        return
    x = int(x)
    for i in range(2, x-1):
        if not x%i:
            prime = False

    return prime

n = input()
array = list(input().split())
for i in array:
    reversed = reverse(i)
    if isPrime(reversed):
        print(reversed, end = ' ')
