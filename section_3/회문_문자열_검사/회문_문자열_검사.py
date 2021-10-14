n = int(input())

for _ in range(n):
    word = input()
    word = word.lower()
    if word == word[::-1]:
        print('YES')
    else:
        print('NO')
