def reverse(x):
    reversed = x[::-1]
    return int(reversed)

def isPrime(x):
    prime = True
    if x == 1:
        return False ## 1 is not a prime
    x = int(x)
    for i in range(2, x-1):  ## 절반까지만 돌면 된다! ex. (1*16) (2*8) (4,4) 
                             ## for i in range(2, x//2+1)
        if not x%i:
            prime = False

    return prime

n = input()
array = list(input().split())
for i in array:
    reversed = reverse(i)
    if isPrime(reversed):
        print(reversed, end = ' ')

 
########### SOLUTION ##############
# reverse를 수학적으로 해결
# isPrime이 더 간결

def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t. # res에 10을 곱해주어야 이전에 결과값이 한자리씩 올라감
        x=x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1):
        if x%i==0:
            return False
    else:
        return True
