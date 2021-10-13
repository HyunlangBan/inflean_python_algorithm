n = input()
array = list(input().split())
for i in array:
    reversed = reverse(i)
    if isPrime(reversed):
        print(reversed, end = ' ')
